
from datetime import datetime 
import os 
import json 
class Transaction():
    def __init__(self, montant, categorie, date=None, description=""):
        self.montant = montant
        self.categorie = categorie
        self.description = description
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")