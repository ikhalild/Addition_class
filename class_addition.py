# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 08:42:13 2022

@author: idial
"""

list_nombres = [1,2,3,4,5,6,7,8]

class Addition:
    
    def __init__(self, nombres):
        self.nombres = nombres
        
    def validate (self):
        for n in self.nombres:
            if isinstance(n, (int, float)):
                self.valide = True
            else:
                self.valide = False
                raise ValueError("Entrez un nombres valide s'il vous plaît.")
                
                
    def sum(self):
        self.some = 0
        for i in self.nombres:
            self.some += i
            return self.some
        
        
    def affiche_somme(self):
        print(f"La somme des {self.nombres} est : {self.some}.")
        
        
somme_nombres = Addition(list_nombres)
somme_nombres.validate()
somme_nombres.sum()
somme_nombres.affiche_somme()        
        