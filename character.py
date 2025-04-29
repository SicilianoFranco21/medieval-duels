from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, name: str, health: int, energy: int, attack: int, defense: int) -> None:
        self._name = name
        self._health = health
        self._energy = energy
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
    def energy(self) -> int:
        return self._energy
    
    @energy.setter
    def energy(self, new_energy: int) -> None:
        self._energy = new_energy

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
    
    def _receive_damage(self, damage: int) -> int:
        actual_damage: int = max(0, (damage - self.defense))
        self.health = max(0, (self.health - actual_damage))
        return actual_damage

    def perform_attack(self, target: 'Character') -> int:
        energy_cost: int = 10
        if self.energy < energy_cost:
            return 0
        self.energy = max(0, (self.energy - energy_cost))
        inflicted_damage: int = target._receive_damage(self.attack)
        return inflicted_damage
    
    def is_alive(self) -> bool:
        return self.health > 0
    
    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass