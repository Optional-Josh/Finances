from anchor_gui import Top_Frame, Bottom_Frame
import customtkinter as ctk


class Main_Window(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Finance Tracker") # set window title name

        # height and width configuration to ensure when window is created, it is placed in the center of the screen
        height = 900
        width = 900
        x = (self.winfo_screenwidth()//2) - (width//2)
        y = (self.winfo_screenheight()//2) - (width//2) + (-50)
        self.geometry("{}x{}+{}+{}".format(width, height, x, y)) # set window width, height and computed values
        self.iconbitmap("logo.ico")

        # calling other frame objects
        self.top_frame = Top_Frame(self) # create top frame object into window
        self.bottom_frame = Bottom_Frame(self, self.top_frame) # create bottom frame object into window with top frame as parameter


if __name__ == "__main__":
    # create an object instance
    window = Main_Window()
    window.mainloop()