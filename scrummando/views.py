# -*- coding: utf-8 -*-

from pyramid.response import Response
from pyramid.view import view_config
from pyramid.security import remember, forget, authenticated_userid
from sqlalchemy.exc import DBAPIError
from pyramid.httpexceptions import HTTPFound, exception_response

from .models import (

    DBSession,
    Users,
    Questions,
    )
import transaction



@view_config(route_name='home', renderer='templates/index.pt')
def index(request):
    questoes = DBSession.query(Questions).all()
    return {"questoes": questoes, "logged" : authenticated_userid(request)}


@view_config(name='add_user', renderer='json')
def add_user(request):
    user_data = request.POST
    new_user = Users(user_data["username"],user_data["password"])
    DBSession.add(new_user)
    transaction.commit()
    return {'status': 'ok'}

@view_config(name='list_users', renderer='templates/list_users.pt')
def list_users(request):
    users = DBSession.query(Users).all()
    return {'users': users}

@view_config(name='login_user', renderer='json')
def login_user(request):
    user_data = request.POST
    user = DBSession.query(Users).filter_by(username=user_data["username"]).first()
    if not user:
        return {'status': 'Nenhum Usuário com este nome',"logged" : False}
    if user.password != user_data["password"]:
        return {'status':'Senha incorreta',"logged" : False}
    else:
        headers = remember(request,user.username)
        return {'status': 'Usuário logado', "logged" : True,"cookies": headers}

@view_config(name='logout', renderer='string')
def logout_server(request):
    """iFeel 2.0:  Function logout user

    """
    headers = forget(request)
    return HTTPFound(location=request.resource_url(request.context), headers=headers)

conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_scrummando_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

