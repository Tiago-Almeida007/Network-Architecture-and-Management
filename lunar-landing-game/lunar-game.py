#!/usr/bin/python3
import sys
from asterisk.agi import AGI # Necessário instalar a biblioteca python-asterisk

agi = AGI()

altitude = 2350.0
velocity = -470.0
fuel = 600
g = -5.0
time_interval = 1

agi.verbose("Iniciando Jogo Lunar Landing")

while altitude > 0 and fuel > 0:
    # 1. Informar o estado ao utilizador (Voz)
    agi.say_number(int(altitude))
    agi.say_number(int(velocity))
    agi.say_number(fuel)

    # 2. Obter entrada DTMF (máximo 10 segundos)
    # 'add_fuel' é um ficheiro de som a dizer "Introduza combustível"
    burn_digits = agi.get_data('add_fuel', timeout=10000, max_digits=2) #TODO: CRIAR FICHEIRO add_fuel usando uma text-to-speech ai qualquer
    
    try:
        burn = int(burn_digits) if burn_digits else 0
    except ValueError:
        burn = 0

    # 3. Lógica matemática (fornecida no seu ficheiro txt) 
    if burn > 75: burn = 75
    if burn > fuel: burn = fuel
    
    fuel -= burn
    # Fórmula: x[n]=x[n-1]+V[n-1].t+(A[n]+G).t^2/2 
    altitude = altitude + velocity * time_interval + (burn + g) * (time_interval**2) / 2.0
    velocity = velocity + (burn + g) * time_interval

# 4. Finalização (Pouso ou Crash) TODO: REVER ESTA PARTE. (N SEI OQ É)
if altitude <= 0:
    if velocity == 0:
        agi.stream_file('congratulations')
    else:
        agi.stream_file('crashed')
