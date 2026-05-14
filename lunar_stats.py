#!/usr/bin/python3
import sys

class SimpleAGI:
    def __init__(self):
        while True:
            linha = sys.stdin.readline().strip()
            if not linha: break

    def _comando(self, cmd):
        sys.stdout.write(cmd + '\n')
        sys.stdout.flush()
        return sys.stdin.readline().strip()

    def get_variable(self, var):
        res = self._comando(f'GET VARIABLE {var}')
        return res.split('(')[1].split(')')[0] if "(" in res else "0"

    def say_number(self, numero):
        self._comando(f'SAY NUMBER {numero} ""')

    def stream_file(self, ficheiro):
        self._comando(f'STREAM FILE {ficheiro} ""')

agi = SimpleAGI()


wins_sessao = agi.get_variable("LUNAR_WINS")
loss_sessao = agi.get_variable("LUNAR_LOSSES")


try:
    with open("/tmp/lunar_global.txt", "r") as f:
        g_vitorias, g_derrotas = f.read().split(",")
except:
    g_vitorias, g_derrotas = "0", "0"


# Sessão
agi.stream_file('current-session-stats') 
agi.stream_file('wins')
agi.say_number(int(wins_sessao))
agi.stream_file('losses')
agi.say_number(int(loss_sessao))

# Globais
agi.stream_file('all-time-stats')
agi.stream_file('wins')
agi.say_number(int(g_vitorias))
agi.stream_file('losses')
agi.say_number(int(g_derrotas))
