from warrior import Warrior
from action_status import ActionStatus
from unittest import TestCase


class TestWarrior(TestCase):
    def setUp(self) -> None:
        """Set up two Warrior instances for testing."""
        self.attacker: Warrior = Warrior("W-attacker")
        self.target: Warrior = Warrior("W-defender")
    
    def test_perform_attack_reduces_target_health(self) -> None:
        """Reduces target's health when attack power exceeds defense."""
        health_before: int = self.target.health
        self.attacker.attack = 50
        self.attacker.perform_attack(self.target)
        self.assertLess(self.target.health, health_before)
    
    def test_perform_attack_reduces_attacker_energy(self) -> None:
        """Reduces attacker's energy after performing an attack."""
        energy_before: int = self.attacker.energy
        self.attacker.perform_attack(self.target)
        self.assertLess(self.attacker.energy, energy_before)
    
    def test_perform_attack_with_no_energy(self) -> None:
        """Returns INSUFFICIENT_ENERGY if attacker has no energy."""
        self.attacker.energy = 0
        attack_attemp: int = self.attacker.perform_attack(self.target)
        self.assertEqual(attack_attemp, ActionStatus.INSUFFICIENT_ENERGY)
    
    def test_perform_attack_successfully(self) -> None:
        """Returns actual damage dealt when energy is sufficient."""
        self.attacker.attack = 50
        expected_damage: int = max(0, self.attacker.attack - self.target.defense)
        attack_attemp: int = self.attacker.perform_attack(self.target)
        self.assertEqual(attack_attemp, expected_damage)
        
    def test_perform_attack_without_inflict_damage(self) -> None:
        """Returns NO_DAMAGE_RECEIVED when attack is too weak or fully blocked by defense."""
        attack_attemp: int = self.attacker.perform_attack(self.target)
        self.assertEqual(attack_attemp, ActionStatus.NO_DAMAGE_RECEIVED)
    
    def test_is_alive_false(self) -> None:
        """Returns False when character's health is zero."""
        self.target.health = 0
        is_target_alive: bool = self.target.is_alive()
        self.assertFalse(is_target_alive)

    def test_is_alive_true(self) -> None:
        """Returns True when character's health is above zero."""
        is_target_alive: bool = self.target.is_alive()
        self.assertTrue(is_target_alive)
    
    def test_repr_(self) -> None:
        """Returns correct __repr__ output for a Warrior."""
        expected_output: str = (f"Warrior(name={self.attacker.name!r}, health={self.attacker.health!r}, energy={self.attacker.energy!r}, "
                                f"attack={self.attacker.attack!r}, defense={self.attacker.defense!r})")
        self.assertEqual(expected_output, repr(self.attacker))
    
    def test_str(self) -> None:
        """Returns readable __str__ description of a Warrior."""
        expected_output: str = (f"{self.attacker.name} is a Warrior with {self.attacker.health} health, {self.attacker.energy} energy, "
                                f"{self.attacker.attack} attack, and {self.attacker.defense} defense.")
        self.assertEqual(expected_output, str(self.attacker))