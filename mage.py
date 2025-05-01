from character import Character
from action_status import ActionStatus


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
    def ENERGY_COST(self) -> int:
        return 10
    
    @property
    def MANA_COST(self) -> int:
        return 25

    @property
    def mana(self) -> int:
        return self._mana
    
    @mana.setter
    def mana(self, new_mana: int) -> None:
        self._mana = new_mana

    def _calculate_inflicted_magical_damage(self, buff: int) -> int:
        buff = max(1, buff)
        magical_damage: int = (self.attack*buff)
        return magical_damage
        
    def _deduct_mana(self) -> None:
        self.mana = max(0, self.mana - self.MANA_COST)
    
    def _check_mana_status(self) -> int:
        if self.mana < self.MANA_COST:
            return ActionStatus.INSUFFICIENT_MANA
        
        self._deduct_mana()
        return ActionStatus.SUCCESS

    def cast_magic_attack(self, target: Character, buff: int) -> int:
        energy_status: int = self._check_energy_status()
        if energy_status != ActionStatus.SUCCESS:
            return energy_status
        
        mana_status: int = self._check_mana_status()
        if mana_status != ActionStatus.SUCCESS:
            return mana_status
        
        raw_magical_damage: int = self._calculate_inflicted_magical_damage(buff)
        inflicted_damage: int = target.receive_damage(raw_magical_damage)
        return inflicted_damage
    
    def __repr__(self) -> str:
        return (f"Mage(name={self.name!r}, mana={self.mana!r}, health={self.health!r}, "
                f"energy={self.energy!r}, attack={self.attack!r}, defense={self.defense!r})")

    def __str__(self) -> str:
        return (f"{self.name} is a Mage with {self.health} health, {self.mana} mana, "
                f"{self.energy} energy, {self.attack} attack, and {self.defense} defense.")