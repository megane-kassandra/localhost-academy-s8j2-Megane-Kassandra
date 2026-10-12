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
        
    def show_info(self):
        print (f" Vehicule : { self . brand } { self . model } {self.doors} portes" )
        
    
class Motorbike(Vehicule):
    def __init__(self, brand, model, engine_size):
        super().__init__(brand, model)
        self.engine_size = engine_size
        
    def show_info(self):
            print (f" Vehicule : { self . brand } { self . model } {self.engine_size} cc" )
            
            
vehicles = [
Car ( " Toyota " , " Corolla " , 4) ,
Motorbike ( " Yamaha " , " MT -07 " , 689) ,
Car ( " Honda " , " Civic " , 4)
]

for vehicle in vehicles :
    vehicle.show_info ()


# Python n’exécute pas la méthode show_info() de Vehicle
# pour un objet Car parce que la methode a ete redefinie 
# dans l'objet Car 