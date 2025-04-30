from character import Character


class Warrior(Character):
    def __init__(
        self, 
        name: str, 
        health: int = 125, 
        energy: int = 125, 
        attack: int = 25, 
        defense: int = 25
        ) -> None:
        super().__init__(name, health, energy, attack, defense)
    
    @property
    def ENERGY_COST(self) -> int:
        return 5
        
    def __repr__(self) -> str:
        return (f"Warrior(name={self.name!r}, health={self.health!r}, energy={self.energy!r}, "
                f"attack={self.attack!r}, defense={self.defense!r})")

    def __str__(self) -> str:
        return (f"{self.name} is a Warrior with {self.health} health, {self.energy} energy, "
                f"{self.attack} attack, and {self.defense} defense.")