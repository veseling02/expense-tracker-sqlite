class Transaction:
    def __init__(self, type, category, item, amount, date, id=None):
        self.id = id
        self.type = type
        self.category = category
        self.item = item
        self.amount = amount
        self.date = date

    def __repr__(self):
        return f"ID: {self.id} | Type: {self.type} | Category: {self.category} | Item: {self.item} | Amount: {self.amount} | Date: {self.date}"