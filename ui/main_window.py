import time

import customtkinter

import timer

customtkinter.set_appearance_mode("System")  # "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # "blue" (standard), "green", "dark-blue"
# TODO potential convertation to str needed
# TODO change functionality to wait and then switch off so if you kill the program it stops the execution
OPTION_ONE = 15
OPTION_TWO = 30
OPTION_THREE = 60
WIDTH = 300
HEIGHT = 400
FONT = ("None", 20)


class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # set up the window
        self.title("Sleep Timer App")
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.minsize(WIDTH, HEIGHT)
        self.maxsize(WIDTH, HEIGHT)

        # manual time entry
        self.entry = customtkinter.CTkEntry(
            master=self, width=200, font=FONT, placeholder_text="Enter time (mins)"
        )
        self.entry.grid(row=1, padx=50, pady=10)

        # buttons
        self.button_one = customtkinter.CTkButton(
            master=self,
            width=200,
            font=FONT,
            fg_color="transparent",
            border_width=2,
            text_color=("green"),
            text=f"{OPTION_ONE} mins",
            command=self.sleep_option_one,
        )
        self.button_one.grid(row=3, pady=10)

        self.button_two = customtkinter.CTkButton(
            master=self,
            width=200,
            font=FONT,
            fg_color="transparent",
            border_width=2,
            text_color=("yellow"),
            text=f"{OPTION_TWO} mins",
            command=self.sleep_option_two,
        )
        self.button_two.grid(row=4, pady=10)

        self.button_three = customtkinter.CTkButton(
            master=self,
            width=200,
            font=FONT,
            fg_color="transparent",
            border_width=2,
            text_color=("red"),
            text=f"{OPTION_THREE} mins",
            command=self.sleep_option_three,
        )
        self.button_three.grid(row=5, pady=10)

        # labels
        self.label_1 = customtkinter.CTkLabel(master=self, width=100, font=("None", 40))
        self.label_1.grid(row=0, pady=50)

    def time_label(self):
        string = timer.clock_24()
        self.label_1.configure(text=string)
        self.label_1.after(1000, self.time_label)

    def sleep_option_one(self):
        time.sleep(5)
        print(timer.switch_off_timer("shutdown", "/r", "/f", "/t", "0"))

    def sleep_option_two(self):
        print(timer.switch_off_timer("echo", "5"))

    def sleep_option_three(self):
        print(timer.switch_off_timer("whoami", "/all"))
