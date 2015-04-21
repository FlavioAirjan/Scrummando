# -*- coding: utf-8 -*-

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Users,
    Questions,
    )
import transaction



@view_config(route_name='home', renderer='templates/index.pt')
def index(request):
    users = DBSession.query(Users).all()
    questoes = DBSession.query(Questions).all()
    return {'users': users, "questoes": questoes}

@view_config(name='add_user', renderer='json')
def add_user(request):
    user_data = request.POST
    new_user = Users(user_data["username"],user_data["password"])
    DBSession.add(new_user)
    transaction.commit()
    return {'status': 'ok'}

@view_config(name='login_user', renderer='json')
def login_user(request):
    user_data = request.POST
    user = DBSession.query(Users).filter_by(username=user_data["username"]).first()
    if not user:
        return {'status': 'Nenhum Usuário com este nome'}
    if user.password != user_data["password"]:
        return {'status':'Senha incorreta'}
    else:
        return {'status': 'Usuário logado'}


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

