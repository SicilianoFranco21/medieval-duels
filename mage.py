from character import Character


class Mage(Character):
    def __init__(
        self, 
        name: str, 
        mana: int = 100, 
        health: int = 100, 
        energy: int = 100, 
        attack: int = 5, 
        defense: int = 10
        ) -> None:
        super().__init__(name, health, energy, attack, defense)
        self._mana = mana
    
    @property
    def mana(self) -> int:
        return self._mana
    
    @mana.setter
    def mana(self, new_mana: int) -> None:
        self._mana = new_mana
    
    def cast_magic_attack(self, target: Character) -> None:
        energy_cost: int = 5
        mana_cost: int = 25
        if not target.is_alive():
            print(f"{target.name} is dead. (x_x)")
            return
        if self.energy < energy_cost:
            print(f"Not enough energy to perform the attack")
            return
        if self.mana < mana_cost:
            print(f"Not enough mana to perform the attack")
            return
        self.energy = max(0, self.energy - energy_cost)
        self.mana = max(0, self.mana - mana_cost)
        magical_damage: int = (self.attack)*10
        target.receive_damage(magical_damage)
        print(f"{self.name} cast a spell on {target.name}")
    
    def __repr__(self) -> str:
        return (f"Mage(name={self.name!r}, mana={self.mana!r}, health={self.health!r}, "
                f"energy={self.energy!r}, attack={self.attack!r}, defense={self.defense!r})")

    def __str__(self) -> str:
        return (f"{self.name} is a Mage with {self.health} health, {self.mana} mana, "
                f"{self.energy} energy, {self.attack} attack, and {self.defense} defense.")