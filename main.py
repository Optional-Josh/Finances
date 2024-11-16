from anchor_gui import Top_Frame, Bottom_Frame
import customtkinter as ctk


class Main_Window(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Finance Tracker") # set window title name
        self.geometry("800x800") # set window width and height

        # calling other frame objects
        self.top_frame = Top_Frame(self) # create top frame object into window
        self.bottom_frame = Bottom_Frame(self, self.top_frame) # create bottom frame object into window with top frame as parameter


if __name__ == "__main__":
    # create an object instance
    window = Main_Window()
    window.mainloop()