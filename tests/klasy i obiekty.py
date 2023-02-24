class Czlowiek:
    imie = 'Wojtek'
    
    def przedstaw_sie(self):
        return 'cześć mam na imie ' + self.imie
        

obiekt = Czlowiek()
print(obiekt.imie)
print(obiekt.przedstaw_sie())


