class Employee:
    def __init__(self, naam, id, leeftijd):
        self.naam = naam.lower()
        self.id = id
        self.leeftijd = leeftijd / 2
    
    def bedrijfsnaam(self):
        return f"{self.naam}-{self.id}"


class Salesman(Employee):
    def __init__(self, naam, leeftijd, cr, sales):
        super().__init__(naam, cr * sales, leeftijd)
        self.cr = cr
        self.sales = sales

    def berekensalaris(self):
        return self.cr * self.sales

    def bedrijfsnaam(self):
        return f"SM-{self.naam}-{self.id}"

class Marketeer(Employee):
    def geefsalaris(self, salaris):
        self.salaris = salaris
    
    def berekensalaris(self, br):
        return br * self.salaris
    
    def bedrijfsnaam(self):
        return f"MT-{self.naam}-{self.id}"