class Transaction:
    def __init__(self, type, category, amount, date, id=None):
        self.id = id
        self.type = type
        self.category = category
        self.amount = amount
        self.date = date

    def __repr__(self):
        return f"ID: {self.id} | Type: {self.type} | Category: {self.category} | Amount: {self.amount} | Date: {self.date}"