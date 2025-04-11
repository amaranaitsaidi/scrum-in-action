from models.transaction import Transaction

class Income(Transaction):
    def __init__(self,date,origin, type):
        super().__init__(date)
        self.origin = origin
        self.type = type

