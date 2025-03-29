import customtkinter as ctk
import time
from datetime import datetime
from record import Record
from file_manipulation import append_dict_to_json
from data_manipulation import dataframes, graph_data

class Add_Records(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title('Extra Window')
        self.geometry('300x400')

        # creating widgets for second/right container
        # variables starting with entry are entry boxes
        # validate keyword and command in entry amount ensures that inputs are numbers only
        # variables starting with add are buttons that initiate the overwriting of object attributes and are partnered with entry boxes
        self.entry_date = ctk.CTkEntry(self, state="disabled", width=175)
        self.entry_category = ctk.CTkEntry(self, state="disabled", width=175)
        self.entry_description = ctk.CTkEntry(self, state="disabled", width=175)
        self.entry_amount = ctk.CTkEntry(self, state="disabled", width=175, validate="key", validatecommand=(self.register(self.validate_input), "%P"))

        self.add_date = ctk.CTkButton(self, state="disabled", text="Add Date", command=self.add_date_input)
        self.add_category = ctk.CTkButton(self, state="disabled", text="Add Category", command=self.add_category_input)
        self.add_description = ctk.CTkButton(self, state="disabled", text="Add Description", command=self.add_description_input)
        self.add_amount = ctk.CTkButton(self, state="disabled", text="Add Amount", command=self.add_amount_input)
        self.submit_records = ctk.CTkButton(self, state="disabled", text="Submit Records and Save to JSON", command=self.return_records)

        # customization by configuration of widgets for second container
        # self.second_container.configure(fg_color="#FF6500")

        self.add_date.configure(fg_color="#003049", hover_color="#C40C0C", text_color_disabled="#f07167")
        self.add_category.configure(fg_color="#003049", hover_color="#C40C0C", text_color_disabled="#f07167")
        self.add_description.configure(fg_color="#003049", hover_color="#C40C0C", text_color_disabled="#f07167")
        self.add_amount.configure(fg_color="#003049", hover_color="#C40C0C", text_color_disabled="#f07167")
        self.submit_records.configure(fg_color="#003049", hover_color="#C40C0C", text_color_disabled="#f07167")

        # pack widgets of second container
        self.record_label = ctk.CTkLabel(self, text="Add a Record", font=("Arial",20,"bold"))
        ctk.CTkLabel(self, text="Joshua Caguimbal").place(relx=0.99, rely=1, anchor="se")

        # place method for widgets
        self.entry_date.place(relx=0.15, rely=0.20)
        self.entry_category.place(relx=0.15, rely=0.30)
        self.entry_description.place(relx=0.15, rely=0.40)
        self.entry_amount.place(relx=0.15, rely=0.50)

        self.add_date.place(relx=0.60, rely=0.20)
        self.add_category.place(relx=0.60, rely=0.30)
        self.add_description.place(relx=0.60, rely=0.40)
        self.add_amount.place(relx=0.60, rely=0.50)
        self.submit_records.place(relx=0.30, rely=0.70)

        # self.second_container.pack(side="left", expand=True, fill="both")

        # event binds
        # self.second_container.bind("<Button-1>", self.get_pos)

    # method that will allow widgets for adding records
    def add_record(self):
        self.button_record.configure(state="disabled")

        # place "Add Record Label" indicating you can add record now
        self.record_label.place(relx=0.15, rely=0.10)

        # change state of widgets from disabled to normal
        self.entry_date.configure(state="normal")
        self.add_date.configure(state="normal")

        self.entry_category.configure(state="normal")
        self.add_category.configure(state="normal")

        self.entry_description.configure(state="normal")
        self.add_description.configure(state="normal")

        self.entry_amount.configure(state="normal")
        self.add_amount.configure(state="normal")

        # empty the contents for entry widgets
        # in case add records and planning to add again
        self.entry_date.delete(0, ctk.END)
        self.entry_category.delete(0, ctk.END)
        self.entry_description.delete(0, ctk.END)
        self.entry_amount.delete(0, ctk.END)

        # final button for submitting is returned to normal
        self.submit_records.configure(state="normal")

    # entry and button for date records setting and validation
    def add_date_input(self):
        entry_date = self.entry_date.get()
        if entry_date == "":
            self.date = time.strftime("%m-%d-%Y", time.localtime())

            # print to top label
            self.top_frame.update_label(f"Date: {self.date} is recorded")

            self.entry_date.configure(state="disabled")
            self.add_date.configure(state="disabled")
        else:
            try:
                validated_date = datetime.strptime(entry_date, "%m-%d-%Y")
                self.date = validated_date.strftime("%m-%d-%Y")

                self.top_frame.update_label(f"Date: {self.date} is recorded")

                self.entry_date.configure(state="disabled")
                self.add_date.configure(state="disabled")
            except ValueError:
                self.top_frame.update_label("Please input with this format 'MM-DD-YYYY'")

    # entry and button for category records setting and validation
    def add_category_input(self):
        entry_category = self.entry_category.get()
        if entry_category.lower() == 'e':
            self.category = 'Expenses'

            # print to top label
            # self.top_frame.update_label(f"Category: {self.category} is recorded")

            self.entry_category.configure(state="disabled")
            self.add_category.configure(state="disabled")
        elif entry_category.lower() == 'i':
            self.category = 'Income'

            # print to top label
            # self.top_frame.update_label(f"Category: {self.category} is recorded")

            self.entry_category.configure(state="disabled")
            self.add_category.configure(state="disabled")
        else:
            self.top_frame.update_label("Please input e for expense or i for income")

    # entry and button for description records setting and validation
    def add_description_input(self):
        entry_description = self.entry_description.get()
        if entry_description.strip():
            self.description = entry_description

            # print to top label
            # self.top_frame.update_label(f"Description: {self.description} is recorded")

            self.entry_description.configure(state="disabled")
            self.add_description.configure(state="disabled")
        else:
            self.top_frame.update_label("Please provide a description, as description can't be empty")

    # entry and button for amount records setting and validation
    def add_amount_input(self):
        entry_amount = self.entry_amount.get()
        if not entry_amount.strip():  # Check for blank input or whitespace
            self.top_frame.update_label("Please input a valid number")
        else:
            number_entry_amount = int(entry_amount)
            
            self.amount = number_entry_amount

            # print to top label
            # self.top_frame.update_label(f"Amount: {self.amount} is recorded")

            self.entry_amount.configure(state="disabled")
            self.add_amount.configure(state="disabled")

    # function for entry widget to allow numbers only
    def validate_input(self, input_text):
        if input_text.isdigit() or input_text == "":
            return True
        return False
    
    # function to return all newly set values to another class and save to json file
    def return_records(self):
        record = Record(self.date, self.category, self.description, self.amount)
        record_dict = record.to_dict()

        append_dict_to_json(record_dict)
        # print to top label
        # self.top_frame.update_label(
        #     f"Records have been saved to JSON file\nDetails of the record:\nDate: {self.date}\nCategory: {self.category}\nDescription: {self.description}\nAmount: {self.amount}")

        self.submit_records.configure(state="disabled")

        self.button_record.configure(state="normal")

    # function to print relx and rely values
    def get_pos(self, event):
        relx = event.x / self.winfo_width()
        rely = event.y / self.winfo_height()

        print(f"{relx:.2f}, {rely:.2f}")

if __name__ == "__main__":

    def create_window():
        add_record = Add_Records()

    window = ctk.CTk()
    window.geometry('600x400')
    window.title('Multiple Windows')

    button1 = ctk.CTkButton(window, text = 'Open Main Window', command = create_window)
    button1.pack(expand = True)

    window.mainloop()