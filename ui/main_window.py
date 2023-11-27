import customtkinter
import timer

customtkinter.set_appearance_mode("System")  # "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # "blue" (standard), "green", "dark-blue"
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
        self.entry.grid(row=9, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # buttons
        self.button_one = customtkinter.CTkButton(
            master=self,
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            text=f"{OPTION_ONE} mins",
            command=self.sleep_option_one,
        )
        self.button_one.grid(row=10, column=2, padx=(20, 20), pady=(20, 20), sticky="w")

        self.button_two = customtkinter.CTkButton(
            master=self,
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            text=f"{OPTION_TWO} mins",
            command=self.sleep_option_two,
        )
        self.button_two.grid(row=10, column=3, padx=(20, 20), pady=(20, 20), sticky="w")

        self.button_three = customtkinter.CTkButton(
            master=self,
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            text=f"{OPTION_THREE} mins",
            command=self.sleep_option_three,
        )
        self.button_three.grid(
            row=10, column=7, padx=(20, 20), pady=(20, 20), sticky="w"
        )

    def sleep_option_one(self):
        print(timer.switch_off_timer("shutdown"))

    def sleep_option_two(self):
        print(timer.switch_off_timer("whoami"))

    def sleep_option_three(self):
        print(timer.switch_off_timer("whoami", "/all"))
