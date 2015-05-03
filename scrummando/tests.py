# -*- coding: utf-8 -*-

import unittest
import transaction

from pyramid import testing

from .models import DBSession


class TestMyViewSuccessCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        from .models import (
            Base,
            Users,
            )
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
            model = Users(username='joao',password="senha")
            DBSession.add(model)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test_login_users(self):
        from scrummando.views import login_user
        
        #Creating dummy request
        request = testing.DummyRequest()
        request.POST["username"] = "joao"
        request.POST["password"] = "senha"

        info = login_user(request)
        self.assertEqual(info['status'], 'Usuário logado')

    def test_add_users(self):
        from scrummando.views import add_user
        
        #Creating dummy request
        request = testing.DummyRequest()
        request.POST["username"] = "joao"
        request.POST["password"] = "senha"

        info = add_user(request)
        self.assertEqual(info['status'], 'ok')


