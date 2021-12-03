from enum import Enum
from pathlib import Path


class Rest_Rank(Enum):
    high = "Magas ertekeles"
    med = "Kozepes ertekeles"
    low = "Alacsony ertekeles"


class CustomerData:
    def __init__(self, nev, tel, cim, email):
        self.nev = input("nev: ")
        self.tel = input("Tel.: ")
        self.cim = input("cím: ")
        self.email = input("email: ")


class CustomerName:
    def __init__(self):
        self.nev = input("nev: ")


class CustomerTel:
    def __init__(self):
        self.tel = input("Tel.: ")


class CustomerCim:
    def __init__(self):
        self.cim = input("cím: ")


class CustomerEmail:
    def __init__(self):
        self.email = input("email: ")


class Food:
    def __init__(self, type, name, price, oszetevok):
        self.type = type
        self.name = name
        self.price = price
        self.osszetevok = oszetevok

    def p_print(self):
        print("\t", "neve:", self.name, "\t", "típusa:", self.type, "\t", "ár:", self.price, "\t", "összetevők:",
              self.osszetevok)

    def __eq__(self, other):
        if not isinstance(other, Restaurant):
            return NotImplemented

        return self.name == other.name


class Restaurant:

    def __init__(self, name, cim, nyitv, type, rank="med"):
        self.name = name
        self.nyitv = nyitv
        self.cim = cim
        self.foods = []
        self.type = type

        if rank == Rest_Rank.high.name:
            self.rank = Rest_Rank.high.value
        elif rank == Rest_Rank.low.name:
            self.rank = Rest_Rank.low.value
        else:
            self.rank = Rest_Rank.med.value

    def p_print(self):
        print(self.name, self.type, self.nyitv)

    def __eq__(self, other):
        if not isinstance(other, Restaurant):
            return NotImplemented

        return self.name == other.name

    def add_food(self, food: Food):
        if food not in self.foods:
            self.foods.append(food)

    def get_time(self):
        print(self.nyitv)


class App:
    def __init__(self, restsFile=Path("ettermek.txt")):
        self.restsFile = restsFile
        self.restaurants = []

    def get_lines(self):
        if self.restsFile.exists():
            with open(self.restsFile, encoding="utf-8") as file:
                lines = [line.strip().split("*") for line in file.readlines()]
                return lines

    def data_process(self):
        for line in self.get_lines():
            rest = Restaurant(line[0], line[1], line[2], line[3])
            if rest not in self.restaurants:
                self.restaurants.append(rest)

        hibas_food = 0
        for line in self.get_lines():
            try:
                food = Food(line[4], line[5], line[6], line[7])
                rest_name = line[0]
            except:
                hibas_food += 1
                rest_name = None
                food = None

            for rest in self.restaurants:
                if rest.name == rest_name and rest_name != None:
                    rest.add_food(food)

        # print("Hibasok:", hibas_food)

    def print_all(self, besorolas=False):
        test = False
        CustomerRestaurant = None
        while test != True:
            CustomerRestaurant = input("Milyen étteremben szeretnél enni? (olasz, Magyaros, Kínai,görög)")
            for rest in self.restaurants:
                if rest.type == CustomerRestaurant:
                    test = True
                    break
                else:
                    test = False
        test = False
        for rest in self.restaurants:
            if rest.type == CustomerRestaurant:
                rest.p_print()
                print("#Besorolas: ", rest.rank)
                for foo in rest.foods:
                    foo.p_print()
        CustomerFood = None
        while test != True:
            CustomerFood = input("Milyen ételt szeretne fogyasztani? (írja le az étel nevét)")
            for rest in self.restaurants:
                if rest.type == CustomerRestaurant:
                    for food in rest.foods:
                        if food.name == CustomerFood:
                            test = True
                            break
                        else:
                            test = False
        for rest in self.restaurants:
            if rest.type == CustomerRestaurant:
                for food in rest.foods:
                    if food.name == CustomerFood:
                        print("Rendelési adatok: ")
                        print(f"Az étel típusa: {food.type}")
                        print(f"Az étel neve: {food.name}")
                        print(f"Az étel ára: {food.price}Ft")
                        ki = open("Rendeles.txt", "w")
                        print("Személyes adatok: \n")

                        cnev = input("név: ")
                        while len(cnev) == 0 or cnev.isnumeric() == True or cnev.isspace() == True:
                            cnev = input("rendes nevet adj kérlek: ")
                        ctel = input("tel.: ")
                        while len(ctel) == 0 or ctel.isnumeric() == False or ctel.isspace() == True:
                                ctel = input("rendes telefonszámot adj kérlek: ")
                        ccim = input("cím: ")
                        while len(ccim) == 0 or ccim.isnumeric() == True or ccim.isspace() == True:
                            ccim = input("rendes címet adj kérlek: ")
                        cmail = input("email: ")
                        while len(cmail) == 0 or cmail.isnumeric() == True or cmail.isspace() == True:
                            cmail = input("rendes emailt adj kérlek: ")

                        ki.write(
                            f"Személyes adatok: \n\tNév:{cnev}\n\tTelefonszám: {ctel}\n\tHely: {ccim}\n\tEmail: {cmail}\n"
                        )
                        ki.write(
                            f"Rendelési adatok: \n\tÉtel: \n\t\ttípusa: {food.type} \n\t\tneve: {food.name} \n\t\tára: {food.price} \nKiszállítási idő: 1 óra"
                        )
                        print("Felvettük rendelését!")

    def run(self):
        self.data_process()
        self.print_all(besorolas=True)


if __name__ == '__main__':
    app = App()
    app.run()
