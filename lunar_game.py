#!/usr/bin/python3
import sys


class SimpleAGI:
    def __init__(self):
        
        while True:
            linha = sys.stdin.readline().strip()
            if not linha:
                break

    def _comando(self, cmd):
        sys.stdout.write(cmd + '\n')
        sys.stdout.flush()
        return sys.stdin.readline().strip()

    def verbose(self, mensagem):
        self._comando(f'VERBOSE "{mensagem}" 1')

    def say_number(self, numero):
        self._comando(f'SAY NUMBER {numero} ""')

    def stream_file(self, ficheiro):
        self._comando(f'STREAM FILE {ficheiro} ""')

    def get_data(self, ficheiro, timeout=10000, max_digits=2):
        resposta = self._comando(f'GET DATA {ficheiro} {timeout} {max_digits}')
        if "result=" in resposta:
            valor = resposta.split("result=")[1].split()[0]
            if valor and valor != '-1':
                return valor
        return ""


agi = SimpleAGI()

altitude = 2350.0
velocity = -470.0
fuel = 600
g = -5.0
time_interval = 1

agi.verbose("Iniciando Jogo Lunar Landing")

while altitude > 0 and fuel > 0:
    
    agi.stream_file('current-altitude')
    agi.say_number(int(altitude))
    agi.stream_file('current-velocity')
    if velocity<0:
        agi.stream_file('negative')
        agi.say_number(int(abs(velocity)))
    else:
        agi.say_number(int(abs(velocity)))
    
    agi.stream_file('current-fuel')
    agi.say_number(int(fuel))

    
    burn_digits = agi.get_data('insert-fuel', timeout=10000, max_digits=2)
    agi.stream_file('burning')
    agi.say_number(int(burn_digits))
    agi.stream_file('liters-fuel')
    
    
    try:
        burn = int(burn_digits) if burn_digits else 0
    except ValueError:
        burn = 0

    agi.verbose(f"Combustivel a queimar: {burn}")

    
    if burn > 75: burn = 75
    if burn > fuel: burn = fuel
    
    fuel -= burn
    
    altitude = altitude + velocity * time_interval + (burn + g) * (time_interval**2) / 2.0
    velocity = velocity + (burn + g) * time_interval


if altitude <= 0:
    if abs(velocity) < 0.1:
        agi.verbose("Pouso Perfeito!")
        agi.stream_file('congratulations')
    else:
        agi.verbose(f"Crash! Velocidade: {velocity}")
        agi.stream_file('crashed')
        agi.stream_file('crash-speed')
        agi.say_number(int(velocity))
