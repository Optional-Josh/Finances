import time
import sys
import customtkinter as ctk
from datetime import datetime
from record import Record
from file_manipulation import append_dict_to_json
from data_manipulation import dataframes, graph_data


class Top_Frame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent) # inherits methods from ctk.CTkFrame and sets the master for the frame from parent parameter

        # creating widgets
        self.label = ctk.CTkLabel(self, text="Welcome", wraplength=700, justify="center", anchor="center", font=("Courier", 20), height=500, width=500)
        self.label.pack(expand=True, fill="both")

        # configure customization
        self.configure(fg_color="#344e41")
        self.configure(fg_color="transparent")

        # pack frame itself
        self.pack(side="top", expand=True, fill="both")

    # class method that changes content of frame in this class, will be called if needed from other classes
    def update_label(self, content):
        self.label.configure(text = content)

class Bottom_Frame(ctk.CTkFrame):
    def __init__(self, parent): # alongside parent as parameter, top_frame is a parameter to reference it, whenever instantiated
        super().__init__(parent) # inherits methods from ctk.CTkFrame and sets the master for the frame from parent parameter

        # object attributes which will be overwritten whenever adding a record
        self.date = None
        self.category = None
        self.description = None
        self.amount = None

        # reference other classes
        # self.top_frame = top_frame

        # invoke class method to create widgets
        self.bottom_frame_widgets()

        # pack frame itself
        self.pack(side="top", expand=True, fill="both")

    # function to compile widget and frame creations
    def bottom_frame_widgets(self):
        # frame container for buttons
        self.first_container = ctk.CTkFrame(self)
        self.second_container = ctk.CTkFrame(self)

        # creating widgets for first/left container
        first_button_container = ctk.CTkFrame(self.first_container)
        ctk.CTkLabel(first_button_container, text="Main Menu", anchor="s", fg_color="transparent", font=("Arial",20,"bold")).pack(pady=10, ipady=5)

        self.button_record = ctk.CTkButton(first_button_container, text="Add a Record", command=self)
        self.button_read = ctk.CTkButton(first_button_container, text="Read Records", command=self.read_json_content)
        self.button_data = ctk.CTkButton(first_button_container, text="Data Analytics", command=graph_data)
        self.button_quit = ctk.CTkButton(first_button_container, text="Quit", command=self.quit_app)

        # customization by configuration of widgets for first container
        self.first_container.configure(fg_color="#FF8A08")
        first_button_container.configure(fg_color="transparent")

        self.button_record.configure(fg_color="#003049", hover_color="#C40C0C", text_color_disabled="#f07167")
        self.button_read.configure(fg_color="#003049", hover_color="#C40C0C", text_color_disabled="#f07167")
        self.button_data.configure(fg_color="#003049", hover_color="#C40C0C", text_color_disabled="#f07167")
        self.button_quit.configure(fg_color="#003049", hover_color="#C40C0C", text_color_disabled="#f07167")

        # packing widgets of first container
        self.button_record.pack(pady=5, expand=True)
        self.button_read.pack(pady=5, expand=True)
        self.button_data.pack(pady=5, expand=True)
        self.button_quit.pack(pady=5, expand=True)

        first_button_container.pack(expand=True, fill="both")

        # pack frame containers
        self.first_container.pack(side="left", expand=True, fill="both")




    # function that runs another function converted json contents to dataframe
    def read_json_content(self):
        data = dataframes()

        # print to top label
        self.top_frame.update_label(data)

    # yet to be implemented function for opening mattplotlib
    def data_analytics(self):
        pass

    # quits overall system running
    def quit_app(self):
        sys.exit()

