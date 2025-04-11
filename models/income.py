from models.transaction import Transaction

class Income(Transaction):
    def __init__(self,montant, origin, date=None, description="") :
        super().__init__(montant, date, description)
        self.origin = origin
        self.type = "revenu"

