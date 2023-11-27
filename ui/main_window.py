import customtkinter

import timer

customtkinter.set_appearance_mode("System")  # "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # "blue" (standard), "green", "dark-blue"
# TODO potential convertation to str needed
OPTION_ONE = 15
OPTION_TWO = 30
OPTION_THREE = 60


class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # set up the window
        self.title("Sleep Timer App")
        self.geometry(f"{700}x{500}")
        self.minsize(400, 400)

        # manual time entry
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter time (mins)")
        self.entry.grid()

        # buttons
        self.button_one = customtkinter.CTkButton(
            master=self,
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            text=f"{OPTION_ONE} mins",
            command=self.sleep_option_one,
        )
        self.button_one.grid()

        self.button_two = customtkinter.CTkButton(
            master=self,
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            text=f"{OPTION_TWO} mins",
            command=self.sleep_option_two,
        )
        self.button_two.grid()

        self.button_three = customtkinter.CTkButton(
            master=self,
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            text=f"{OPTION_THREE} mins",
            command=self.sleep_option_three,
        )
        self.button_three.grid()

        self.button_clock = customtkinter.CTkButton(
            master=self,
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            text=timer.clock_24(),
        )
        self.button_clock.grid()

        # view
        self.current_view = customtkinter.CTkFrame(
            self, width=100, fg_color="transparent"
        )

        # labels
        self.current_label = customtkinter.CTkLabel(
            self.current_view,
            text="Current Operations",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )

    def clock_label(self):
        self.current_label = customtkinter.CTkLabel(
            self.current_view,
            text=timer.clock_24(),
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.current_label.grid()

    def sleep_option_one(self):
        print(timer.switch_off_timer("shutdown"))

    def sleep_option_two(self):
        print(timer.switch_off_timer("echo", "5"))

    def sleep_option_three(self):
        print(timer.switch_off_timer("whoami", "/all"))


# row=9, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew"
# row=10, column=3, padx=(20, 20), pady=(20, 20), sticky="w"
