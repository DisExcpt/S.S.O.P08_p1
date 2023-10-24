import random

class Estacionamiento:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.estado = ["libre"] * capacidad  # Inicialmente, todos los espacios están libres
        self.autos = []

    def agregar_auto(self):
        espacios_libres = [i for i, estado in enumerate(self.estado) if estado == "libre"]
        if espacios_libres:
            idx = random.choice(espacios_libres)  # Seleccionar un espacio libre aleatorio
            self.autos.append(idx)  # Agregar el índice del espacio ocupado
            self.estado[idx] = "ocupado"

    def retirar_auto(self):
        if self.autos:
            idx = self.autos.pop(0)  # Retirar el auto del espacio más antiguo
            self.estado[idx] = "libre"

