from character import Character


class Mage(Character):
    _MANA_COST: int = 25
    
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
    def ENERGY_COST(self) -> int:
        return 10

    @property
    def mana(self) -> int:
        return self._mana
    
    @mana.setter
    def mana(self, new_mana: int) -> None:
        self._mana = new_mana

    def _calculate_magical_damage(self, buff: int) -> int:
        buff = max(1, buff)
        magical_damage: int = (self.attack*buff)
        return magical_damage
        
    def _deduct_mana(self) -> None:
        self.mana = max(0, self.mana - self._MANA_COST)
    
    def _check_magical_resources(self) -> int:
        if self.mana < self._MANA_COST:
            return self._ActionStatus.INSUFFICIENT_MANA
        
        self._deduct_mana()
        return self._ActionStatus.SUCCESS

    def cast_magic_attack(self, target: Character, buff: int) -> int:
        resource_status: int = self._check_resources()
        if resource_status != self._ActionStatus.SUCCESS:
            return resource_status
        
        magical_resource_status: int = self._check_magical_resources()
        if magical_resource_status != self._ActionStatus.SUCCESS:
            return magical_resource_status
        
        magical_damage: int = self._calculate_magical_damage(buff)
        inflicted_damage: int = target._receive_damage(magical_damage)
        return inflicted_damage
    
    def __repr__(self) -> str:
        return (f"Mage(name={self.name!r}, mana={self.mana!r}, health={self.health!r}, "
                f"energy={self.energy!r}, attack={self.attack!r}, defense={self.defense!r})")

    def __str__(self) -> str:
        return (f"{self.name} is a Mage with {self.health} health, {self.mana} mana, "
                f"{self.energy} energy, {self.attack} attack, and {self.defense} defense.")