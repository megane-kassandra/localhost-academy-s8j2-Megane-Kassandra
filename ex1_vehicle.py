class Vehicule:
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def show_info(self):
        print (f" Vehicule : { self . brand } { self . model } " )
        
    
class Car(Vehicule):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors
        
    
class Motorbike(Vehicule):
    def __init__(self, brand, model, engine_size):
        super().__init__(brand, model)
        self.engine_size = engine_size
        
    
car = Car ( " Toyota " , " Corolla " , 4)
motorbike = Motorbike ( " Yamaha " , " MT -07 " , 689)

car.show_info()
motorbike.show_info()

# les classes Car et Motorbike peuvent utiliser la méthode show_info() sans la redéfinir 
# car elles heritent de cette methode de la classe Vehicule