import time
import sys
import random
from colorama import Fore, Style, init

init(autoreset=True)

colors = [Fore.CYAN, Fore.MAGENTA, Fore.GREEN, Fore.YELLOW, Fore.BLUE]

def typewriter(text, delay=0.05, color=Fore.CYAN):
    for char in text:
        sys.stdout.write(color + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay)
    print()
print(Fore.CYAN )
time.sleep(0.5)
intro = [
    "姓名:鄒鴻瑋\n",
    "學號:01357035",
]
for line in intro:
    typewriter(line, delay=0.07, color=random.choice(colors))

for dot in "....":
    sys.stdout.write(Fore.YELLOW + dot)
    sys.stdout.flush()
    time.sleep(0.5)
print(" ===")
