from abc import ABC, abstractmethod
from action_status import ActionStatus


class Character(ABC):   
    def __init__(self, name: str, health: int, energy: int, attack: int, defense: int) -> None:
        """
        Initialize a Character with basic attributes.

        :param name: The name of the character.
        :param health: The health value of the character.
        :param energy: The energy value of the character.
        :param attack: The attack power of the character.
        :param defense: The defense value of the character.
        """
        self._name = name
        self._health = health
        self._energy = energy
        self._attack = attack
        self._defense = defense
        self._items: list[str] = []
    
    @property
    @abstractmethod
    def ENERGY_COST(self) -> int:
        """Abstract property that defines the energy cost of performing an action."""
        pass
    
    @property
    def name(self) -> str:
        """Return the character's name."""
        return self._name
    
    @name.setter
    def name(self, new_name: str) -> None:
        """Set a new name for the character."""
        self._name = new_name

    @property
    def health(self) -> int:
        """Return the character's current health."""
        return self._health
    
    @health.setter
    def health(self, new_health: int) -> None:
        """Set a new health value for the character."""
        self._health = new_health

    @property
    def energy(self) -> int:
        """Return the character's current energy."""
        return self._energy
    
    @energy.setter
    def energy(self, new_energy: int) -> None:
        """Set a new energy value for the character."""
        self._energy = new_energy

    @property
    def attack(self) -> int:
        """Return the character's attack value."""
        return self._attack
    
    @attack.setter
    def attack(self, new_attack: int) -> None:
        """Set a new attack value for the character."""
        self._attack = new_attack

    @property
    def defense(self) -> int:
        """Return the character's defense value."""
        return self._defense
    
    @defense.setter
    def defense(self, new_defense: int) -> None:
        """Set a new defense value for the character."""
        self._defense = new_defense

    def _deduct_energy(self) -> None:
        """
        Deduct energy from the character by the amount defined in ENERGY_COST.
        Ensures energy doesn't drop below zero.
        """
        self.energy = max(0, self.energy - self.ENERGY_COST)
    
    def _calculate_received_damage(self, incoming_damage: int) -> int:
        """
        Calculate the actual damage taken after applying defense.

        :param damage: Raw incoming damage.
        :return: Effective damage after defense reduction.
        """
        actual_damage_taken: int = max(0, (incoming_damage - self.defense))
        return actual_damage_taken

    def receive_damage(self, damage: int) -> int:
        """
        Apply damage to the character and reduce health accordingly.

        :param damage: Incoming raw damage.
        :return: Actual damage taken or ActionStatus.NO_DAMAGE_RECEIVED.
        """
        received_damage: int = self._calculate_received_damage(damage)
        if received_damage == 0:
            return ActionStatus.NO_DAMAGE_RECEIVED
        
        self.health = max(0, (self.health - received_damage))
        return received_damage

    def _check_energy_status(self) -> int:
        """
        Check if the character has enough energy to perform an action.

        :return: ActionStatus.SUCCESS if energy is sufficient,
                 otherwise ActionStatus.INSUFFICIENT_ENERGY.
        """
        if self.energy < self.ENERGY_COST:
            return ActionStatus.INSUFFICIENT_ENERGY
        
        self._deduct_energy()
        return ActionStatus.SUCCESS

    def perform_attack(self, target: 'Character') -> int:
        """
        Attack another character, consuming energy and dealing damage.

        :param target: The target character to attack.
        :return: Damage dealt or ActionStatus code if attack fails.
        """
        energy_status: int = self._check_energy_status()
        if energy_status != ActionStatus.SUCCESS:
            return energy_status
        
        inflicted_damage: int = target.receive_damage(self.attack)
        return inflicted_damage
    
    def recover_energy(self) -> None:
        recovered_energy: int = 20
        self.energy += recovered_energy
    
    def is_alive(self) -> bool:
        """
        Check if the character is still alive.

        :return: True if health > 0, False otherwise.
        """
        return self.health > 0
    
    @abstractmethod
    def __repr__(self) -> str:
        """Return the developer-friendly string representation of the character."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Return the user-friendly string representation of the character."""
        pass