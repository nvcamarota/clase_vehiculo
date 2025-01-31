"""
CREAR UNA CLASE "VEHÍCULO"
Crear una clase llamada "Vehículo", con los atributos: marca, modelo y color.
Agregar un método "describir" que imprima los detalles del vehículo.
Crear tres objetos de tipo Vehículo y describirlos.
"""

class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca.capitalize()
        self.modelo = modelo.capitalize()
        self.color = color.lower()
        
    def describir(self):
        return f'Vehículo marca "{self.marca}", modelo {self.modelo} de color {self.color}.'
        
def vehiculos():
    print('\nVehículos a disposición:')
    return [
        Vehiculo('Renault', 'Kangoo', 'Rojo'),
        Vehiculo('Ford', 'Maverick', 'Gris Plata'),
        Vehiculo('Volkswagen', 'Virtus', 'Negro')
    ]
    
for vehiculo in vehiculos():
    print(f'- {vehiculo.describir()}')
    
print('\nEstos fueron los vehículos disponibles con clase Vehículo. GL HF ✨\n')