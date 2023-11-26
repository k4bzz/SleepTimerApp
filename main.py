import subprocess

import customtkinter

customtkinter.set_appearance_mode("dark")

result = subprocess.run(["dir"], shell=True, stdout=subprocess.PIPE, text=True)

if __name__ == "__main__":
    print(result.stdout)

    # ettes
