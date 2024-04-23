from scripts.queries import *
from scripts.models.transaction import Base

if __name__ == '__main__':
    Base.metadata.create_all(get_engine())
    eleccion = input("Que operación desea realizar\n"
                     "1. Cargar todos los datos\n"
                     "2. Cargar las primeras 50 transacciones\n")
    if eleccion == "1":
        cargar()
    elif eleccion == "2":
        cargar_50()
    else:
        print("Valor incorrecto")
