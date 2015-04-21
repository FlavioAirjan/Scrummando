import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models import (
    DBSession,
    Base,
    Questions,
    )


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)

def get_questoes():
    current_dir = os.path.dirname(__file__)
    p_file = open(current_dir + "/../../questoes.txt","r")

    questoes = []
    for line in p_file.readlines():
        questao = []
        line = line.decode("utf-8")
        line = line.replace("\n","")
        line = line.replace("\r","")
        line = line.split("\t")
        questao.append(line[0])
        questao.append(line[1])
        questao.append(line[2])
        questao.append(line[3])
        questao.append(line[4])
        questao.append(int(line[5]))
        questoes.append(questao)
    return questoes



def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    questoes = get_questoes()
    with transaction.manager:
        for questao_data in questoes:
            questao_db = Questions(questao_data)
            DBSession.add(questao_db)
