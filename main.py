import subprocess

import customtkinter

customtkinter.set_appearance_mode("dark")

result = subprocess.run(["dir"], shell=True, stdout=subprocess.PIPE, text=True)


def button_callback():
    print("button pressed")


app = customtkinter.CTk()
app.title("my app")
app.geometry("400x150")

button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20)

app.mainloop()

if __name__ == "__main__":
    print(result.stdout)

    # ettes
