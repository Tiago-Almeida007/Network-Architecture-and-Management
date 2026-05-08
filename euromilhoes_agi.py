#!/usr/bin/env python3

import sys
import re
import requests
from bs4 import BeautifulSoup

def agi(cmd):
    print(cmd)
    sys.stdout.flush()
    return sys.stdin.readline().strip()

def say_number(n):
    agi(f"EXEC SayNumber {int(n)}")

def play(file):
    agi(f"EXEC Playback {file}")

url = "https://www.jogossantacasa.pt/web/SCCartazResult/"

try:
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    text = soup.get_text(" ", strip=True)

    pattern = r"CHAVE.*?(\d{1,2})\s+(\d{1,2})\s+(\d{1,2})\s+(\d{1,2})\s+(\d{1,2})\s*\+\s*(\d{1,2})\s+(\d{1,2})"
    match = re.search(pattern, text, re.IGNORECASE)

    if not match:
        play("invalid")
        sys.exit(0)

    values = list(match.groups())

    numbers = values[:5]
    stars = values[5:7]

    play("the-number-is")

    for n in numbers:
        say_number(n)

    play("and")

    for s in stars:
        say_number(s)

except Exception:
    play("invalid")

sys.exit(0)
