from abc import ABC, abstractmethod
from random import randint


class Personaje(ABC):
    def __init__(self, nombre: str, vida: int, ataque: int, defensa: int) -> None:
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
    
    @abstractmethod
    def show_state(self) -> str:
        return f"{self.nombre} -> Vida: {self.vida} | Ataque: {self.ataque} | Defensa: {self.defensa}"