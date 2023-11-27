import subprocess


def switch_off_timer(*args) -> str:
    command = subprocess.run(args, shell=True, stdout=subprocess.PIPE, text=True)
    return command.stdout
