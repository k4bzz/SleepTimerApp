import subprocess


result = subprocess.run(["dir"], shell=True, stdout=subprocess.PIPE, text=True)
