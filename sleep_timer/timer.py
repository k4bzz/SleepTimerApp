import subprocess
from datetime import datetime


def switch_off_timer(*args: str) -> str:
    command = subprocess.run(args, shell=True, stdout=subprocess.PIPE, text=True)
    return command.stdout


def clock_24():
    now = datetime.now()
    text = now.strftime("%H:%M:%S")
    return text
