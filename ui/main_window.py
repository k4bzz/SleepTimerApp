import customtkinter

customtkinter.set_appearance_mode("System")  # "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # "blue" (standard), "green", "dark-blue"


class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # set up the window
        self.title("Sleep Timer App")
        self.geometry(f"{700}x{500}")
        # self.grid_columnconfigure(1, weight=0)
        # self.grid_columnconfigure((0, 1), weight=0)
        # self.grid_rowconfigure((0, 1, 2), weight=1)

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter time (mins)")
        self.entry.grid(
            row=7, column=7, columnspan=3, padx=(20, 0), pady=(20, 20), sticky="nsew"
        )
        self.main_button_1 = customtkinter.CTkButton(
            master=self,
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            text="blyatt",
        )
        self.main_button_1.grid(
            row=3, column=3, columnspan=5, padx=(20, 20), pady=(20, 20), sticky="w"
        )
