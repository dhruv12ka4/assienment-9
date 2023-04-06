class Dog:
    def __init__(self,name,age,coat_color):

        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f'name : {self.name}\nage :{self.age}\n')

    def get_info(self):
        print(f'coat_color : {self.coat_color}\n')
        

class JackRussellTerrier(Dog):
    def __init_(self,name,age,coat_color,life):
        super().__init__(name,age,coat_color)
        self.life = life

    def all_details(self):
        print(f'name : {self.name}\nage : {self.age}\ncoat_color : {self.coat_color}\nlife : {self.life}\n')

    def breed(self):
        print('\nbreed : JackRussellTerrier\n')


class Bulldog(Dog):
    def __init__(self,name,age,coat_color,weight):
        super().__init__(name,age,coat_color)
        self.weight = weight

    def all_details(self):
        print(f'name : {self.name}\nage : {self.age}\ncoat_color : {self.coat_color}\nweight : {self.weight}kg\n')

    def breed(self):
        print('\nbreed : Bulldog\n')

jackRT = JackRussellTerrier('Harry',10,'Brown',20)
jackRT.all_details()
jackRT.breed()
jackRT.description()
jackRT.get_info()

bulldog = Bulldog('Max',5,'Black',24)
bulldog.all_details()
bulldog.breed()
bulldog.description()
bulldog.get_info()
    
    



