class Record:
    # unique values or attributes for the class
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    # function that converts instance attributes into dictionary
    def to_dict(self):
        return {
            self.date: [
                {
                "category": self.category,
                "description": self.description,
                "amount": self.amount
                }
            ]
        }