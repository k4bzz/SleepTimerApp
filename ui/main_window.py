import customtkinter

customtkinter.set_appearance_mode("System")  # "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # "blue" (standard), "green", "dark-blue"


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
        self.switch_off_15m = customtkinter.CTkButton(
            master=self,
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            text="15 mins",
            command=print("test 15m"),
        )
        self.switch_off_15m.grid(
            row=10, column=2, padx=(20, 20), pady=(20, 20), sticky="w"
        )

        self.switch_off_30m = customtkinter.CTkButton(
            master=self,
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            text="30 mins",
            command=print("test 30m"),
        )
        self.switch_off_30m.grid(
            row=10, column=3, padx=(20, 20), pady=(20, 20), sticky="w"
        )

        self.switch_off_1h = customtkinter.CTkButton(
            master=self,
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            text="1 hr",
            command=print("test 1h"),
        )
        self.switch_off_1h.grid(
            row=10, column=7, padx=(20, 20), pady=(20, 20), sticky="w"
        )
