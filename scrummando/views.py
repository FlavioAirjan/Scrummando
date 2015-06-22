# -*- coding: utf-8 -*-

from pyramid.response import Response
from pyramid.view import view_config
from pyramid.security import remember, forget, authenticated_userid
from sqlalchemy.exc import DBAPIError
from pyramid.httpexceptions import HTTPFound, exception_response
from sqlalchemy import desc


from .models import (

    DBSession,
    Users,
    Questions,
    Games,
    Answers,
    )
import transaction
import random



@view_config(route_name='home', renderer='templates/index.pt')
def index(request):
    questoes = []
    respostas = []
    loaded_game = False
    if request.GET.has_key("g_id"):
        gameLoaded = DBSession.query(Games).filter_by(id=request.GET["g_id"]).first()
        loaded_game = True
        for answer in gameLoaded.answers:
            questao = DBSession.query(Questions).filter_by(id=answer.question_id).first()
            resposta = answer.answer_pos
            respostas.append(resposta)
            questoes.append(questao)
    else:
        questoes = DBSession.query(Questions).all()
        questoes = random.sample(questoes,15)


    username = authenticated_userid(request)
    completed_games = []
    saved_games = []

    if username:
        user = DBSession.query(Users).filter_by(username=username).first()
        if user == None:
            headers = forget(request)
            return HTTPFound(location=request.resource_url(request.context), headers=headers)
        completed_games = DBSession.query(Games).filter_by(user_id=user.id, completed=True).order_by(desc(Games.date)).all()
        saved_games = DBSession.query(Games).filter_by(user_id=user.id, completed=False).order_by(desc(Games.date)).all()


    return {"respostas":respostas,"loaded_game": loaded_game, "questoes": questoes, "logged" : authenticated_userid(request),"completed_games":completed_games,"saved_games":saved_games}


@view_config(name='add_user', renderer='json')
def add_user(request):
    user_data = request.POST
    new_user = Users(user_data["username"],user_data["password"])
    DBSession.add(new_user)
    transaction.commit()
    return {'status': 'ok',"registered":True}

@view_config(name='list_users', renderer='templates/list_users.pt')
def list_users(request):
    ranking = []
    users = DBSession.query(Users).all()
    best_games = []
    for user in users:
        best_game = DBSession.query(Games).filter_by(user_id=user.id, completed=True).order_by(desc(Games.score)).first()
        score = 0 if not best_game else best_game.score
        ranking.append((user.username,score))
    ranking = sorted(ranking, key=lambda item: item[1],reverse=True)
    return {'ranking': ranking}

@view_config(name='list_questions', renderer='templates/list_questions.pt')
def list_questions(request):
    questoes = DBSession.query(Questions).all()
    return {'questoes': questoes}

@view_config(name='delete_game', renderer='json')
def delete_game(request):
    game_id = request.POST["g_id"]
    game = DBSession.query(Games).filter_by(id=game_id).first()
    DBSession.delete(game)
    transaction.commit()
    return {"deleted":True}


@view_config(name='login_user', renderer='json')
def login_user(request):
    user_data = request.POST
    user = DBSession.query(Users).filter_by(username=user_data["username"]).first()
    if not user:
        return {'status': 'Nenhum usuário com este nome',"logged" : False}
    if user.password != user_data["password"]:
        return {'status':'Senha incorreta',"logged" : False}
    else:
        headers = remember(request,user.username)
        return {'status': 'Usuário logado', "logged" : True,"cookies": headers}

@view_config(name='logout', renderer='string')
def logout_server(request):
    headers = forget(request)
    return HTTPFound(location=request.resource_url(request.context), headers=headers)

@view_config(name='save', renderer='json')
def save(request):
    username = authenticated_userid(request)
    user = DBSession.query(Users).filter_by(username=username).first()

    newSave = Games()
    newSave.user_id = user.id
    
    #Get Answes
    list_qID_answer = request.POST.items()
    for value in list_qID_answer:
        db_answer = Answers()
        db_answer.question_id = int(value[0])
        db_answer.answer_pos = int(value[1])
        newSave.answers.append(db_answer)
    newSave.completed = False
    DBSession.add(newSave)
    transaction.commit()    

    return {"game_saved": True}

@view_config(name='submit_answers', renderer='json')
def submit_answers(request):
    username = authenticated_userid(request)
    user = DBSession.query(Users).filter_by(username=username).first()

    newGame = Games()
    score = 0
    newGame.user_id = user.id
    
    #Get Answes
    list_qID_answer = request.POST.items()
    for value in list_qID_answer:
        db_answer = Answers()
        db_answer.question_id = int(value[0])
        db_answer.answer_pos = int(value[1])
        newGame.answers.append(db_answer)

        question = DBSession.query(Questions).filter_by(id=db_answer.question_id).first()
        if question.correct_alternative_pos == db_answer.answer_pos:
            score += 10
    newGame.score = score
    newGame.completed = True
    DBSession.add(newGame)
    transaction.commit()
    return {"game_submitted": True}


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

