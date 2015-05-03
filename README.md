# Scrummando
Aprendendo Scrum de uma forma divertida.

## O que é o Scrummando?

  Scrumando é um jogo com o objetivo de ensinar o modelo de desenvolvimento ágil Scrum para iniciantes. De uma forma interativa e divertida o jogador entrará no mundo do desenvolvimento de software e será guiado por todas as etapas do Scrum, familiarizando com as tecnicas de desenvolvimento ágil.
  
## Objetivo do Trabalho

  Este é um trabalho acadêmico desenvolvido pelo grupo Scrummando do curso de Engenharia de Software da Universidade Federal de Minas Gerais. O objetivo do trabalho é desenvolver um jogo para ensinar conceitos de engenharia de software e em seu desenvolvimento utilizar algum método ágil, neste caso usaremos o própio Scrum.

## Documentação

### Instalação:
Ambiente utilizado: Linux Debien-derived

1.	**Instale o python-setuptools:** 'sudo apt-get install python-setuptools'
2.	**Download Scrummando:** 'git clone https://github.com/FlavioAirjan/Scrummando.git'
3.	**Entre na Pasta criada:** 'cd Scrummando'
4.  **Instale Scrummando no Python:** 'sudo python setup.py develop'
	
### Execução:
1.	**Execute o Scrummando:** 'pserve development.ini'
2.  **Acesse o Scrummando pelo seu browser em:** 'http://0.0.0.0:6543'

### Execução de testes:
#### Testes de Unidade:
1.	**Execute testes de Unidade:** 'sudo python setup.py test -q'

#### Testes Funcionais:
1.	**Deixe o Scrummando executando em:** 'http://0.0.0.0:6543'
2.	**Execute testes funcionais:** 'sudo python selenium_test.py'

Obs: Será usado o navegador chrome então precisa dele instalado.



