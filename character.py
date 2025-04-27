from abc import ABC, abstractmethod
from random import randint


class Character(ABC):
    def __init__(self, name: str, health: int, attack: int, defense: int) -> None:
        self._name = name
        self._health = health
        self._attack = attack
        self._defense = defense
        self._items: list[str] = []
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name

    @property
    def health(self) -> int:
        return self._health
    
    @health.setter
    def health(self, new_health: int) -> None:
        self._health = new_health

    @property
    def attack(self) -> int:
        return self._attack
    
    @attack.setter
    def attack(self, new_attack: int) -> None:
        self._attack = new_attack

    @property
    def defense(self) -> int:
        return self._defense
    
    @defense.setter
    def defense(self, new_defense: int) -> None:
        self._defense = new_defense
    
    @abstractmethod
    def execute_attack(self, other_character: 'Character') -> None:
        pass
    
    @abstractmethod
    def take_damage(self, damage: int) -> None:
        pass
    
    def show_state(self) -> str:
        return f"{self.name} -> health: {self.health} | attack: {self.attack} | defense: {self.defense}"