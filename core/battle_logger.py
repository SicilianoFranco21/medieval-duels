class BattleLogger:
    """Utility class for logging battle actions and events during combat."""

    @staticmethod
    def log_attack(attacker: str, defender: str) -> None:
        """Logs a basic physical attack from the attacker to the defender."""
        print(f"🗡️  {attacker} performed an attack on {defender}")
    
    @staticmethod
    def log_magic_attack(caster: str, target: str) -> None:
        """Logs a magical spell cast from the caster to the target."""
        print(f"✨ {caster} cast a spell on {target}")
    
    @staticmethod
    def log_not_enough_energy_for_attack() -> None:
        """Logs when a character doesn't have enough energy to attack."""
        print("⚠️ Not enough energy to perform the attack")
    
    @staticmethod
    def log_not_enough_mana_for_spell() -> None:
        """Logs when a character doesn't have enough mana to cast a spell."""
        print("⚠️ Not enough mana to cast the spell")
    
    @staticmethod
    def log_target_dead(character: str) -> None:
        """Logs that the given character has died."""
        print(f"☠️ {character} is dead. (x_x)")

    @staticmethod
    def log_target_already_dead(target_label: str) -> None:
        print(f"💀 {target_label} is already dead. The attack was not executed.")
    
    @staticmethod
    def log_damage_received(character: str, amount: int) -> None:
        """Logs the amount of damage received by a character."""
        print(f"💢 {character} took {amount} points of damage")
    
    @staticmethod
    def log_no_damage(character: str) -> None:
        """Logs when a character receives no damage."""
        print(f"🛡️  {character} did not receive any damage")

    @staticmethod
    def log_energy_recovered(character: str, amount: int) -> None:
        """Logs the energy recovery event due to rest."""
        print(f"🛌 {character} rested and recovered {amount} energy points")
