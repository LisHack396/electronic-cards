from scripts.queries import *
from scripts.models.transaction import Base

if __name__ == '__main__':
    Base.metadata.create_all(get_engine())
    eleccion = input("Que operación desea realizar\n"
                     "1. Cargar las primeras 50 transacciones\n")
    if eleccion == "1":
        cargar()
    else:
        print("Valor incorrecto")
