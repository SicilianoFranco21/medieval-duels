from mage import Mage
from unittest import TestCase
from unittest.mock import patch
from io import StringIO


class TestMage(TestCase):
    def setUp(self) -> None:
        self.attacker: Mage = Mage("M-attacker")
        self.target: Mage = Mage("M-target")
    
    def test_cast_magic_attack_reduces_target_health(self) -> None:
        """Test that cast_magic_attack reduces the target's health."""
        pass

    def test_cast_magic_attack_reduces_attacker_energy(self) -> None:
        """Test that cast_magic_attack reduces the attacker's energy."""
        pass

    def test_cast_magic_attack_to_dead_target(self) -> None:
        """Test that cast_magic_attack prints a message if the target is dead."""
        pass

    def test_cast_magic_attack_with_no_energy(self) -> None:
        """Test that cast_magic_attack prints a message if the attacker has no energy."""
        pass

    def test_cast_magic_attack_with_no_mana(self) -> None:
        """Test that cast_magic_attack prints a message if the attacker has no mana."""
        pass

    def test_cast_magic_attack_successfully(self) -> None:
        """Test that cast_magic_attack prints a successful spell cast message."""
        pass

    
    def test_perform_attack_reduces_target_health(self) -> None:
        """Test that perform_attack reduces the target's health."""
        health_before: int = self.target.health
        self.attacker.attack = 50
        self.attacker.perform_attack(self.target)
        self.assertLess(self.target.health, health_before)
    
    def test_perform_attack_reduces_attacker_energy(self) -> None:
        """Test that perform_attack reduces the attacker's energy."""
        energy_before: int = self.attacker.energy
        self.attacker.perform_attack(self.target)
        self.assertLess(self.attacker.energy, energy_before)

    def test_perform_attack_to_dead_target(self) -> None:
        """Test that perform_attack prints a message if the target is dead."""
        self.target.health = 0
        with patch("sys.stdout", new=StringIO()) as fake_stdout:
            self.attacker.perform_attack(self.target)
        self.assertIn(f"{self.target.name} is dead. (x_x)", fake_stdout.getvalue().strip())
    
    def test_perform_attack_with_no_energy(self) -> None:
        """Test that perform_attack prints a message if attacker has no energy."""
        self.attacker.energy = 0
        with patch("sys.stdout", new=StringIO()) as fake_stdout:
            self.attacker.perform_attack(self.target)
        self.assertIn("Not enough energy to perform the attack", fake_stdout.getvalue().strip())
    
    def test_perform_attack_successfully(self) -> None:
        """Test that perform_attack prints a successful attack message."""
        self.attacker.attack = 50
        with patch("sys.stdout", new=StringIO()) as fake_stdout:
            self.attacker.perform_attack(self.target)
        self.assertIn(f"{self.attacker.name} performed an attack on {self.target.name}", fake_stdout.getvalue().strip())
        
    def test_receive_damage_zero_damage(self) -> None:
        """Test that receive_damage prints a message when no damage is taken."""
        with patch("sys.stdout", new=StringIO()) as fake_stdout:
            self.target.receive_damage(self.attacker.attack)
            self.assertIn(f"{self.target.name} did not received any damage", fake_stdout.getvalue().strip())

    def test_receive_damage_successfully(self) -> None:
        """Test that receive_damage prints a message when damage is taken."""
        self.attacker.attack = 50
        with patch("sys.stdout", new=StringIO()) as fake_stdout:
            actual_damage: int = self.target.receive_damage(self.attacker.attack)
            self.assertIn(f"{self.target.name} took {actual_damage} points of damage", fake_stdout.getvalue().strip())
    
    def test_is_alive_true(self) -> None:
        """Test that is_alive returns False when health is 0."""
        self.target.health = 0
        is_target_alive: bool = self.target.is_alive()
        self.assertFalse(is_target_alive)

    def test_is_alive_false(self) -> None:
        """Test that is_alive returns True when health is above 0."""
        is_target_alive: bool = self.target.is_alive()
        self.assertTrue(is_target_alive)
    
    def test_repr_(self) -> None:
        """Test the __repr__ method for the Warrior class."""
        expected_output: str = (f"Mage(name={self.attacker.name!r}, mana={self.attacker.mana!r}, health={self.attacker.health!r}, "
                                f"energy={self.attacker.energy!r}, attack={self.attacker.attack!r}, defense={self.attacker.defense!r})")
        self.assertEqual(expected_output, repr(self.attacker))
    
    def test_str(self) -> None:
        """Test the __str__ method for the Warrior class."""
        expected_output: str = (f"{self.attacker.name} is a Mage with {self.attacker.health} health, {self.attacker.mana} mana, "
                f"{self.attacker.energy} energy, {self.attacker.attack} attack, and {self.attacker.defense} defense.")
        self.assertEqual(expected_output, str(self.attacker))