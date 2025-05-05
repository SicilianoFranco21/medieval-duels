class BattleLogger:
    """Utility class for logging battle actions and events during combat."""

    @staticmethod
    def log_attack(attacker_name: str, target_name: str) -> None:
        """Logs a basic physical attack from the attacker to the target."""
        print(f"🗡️  {attacker_name} performed an attack on {target_name}")
    
    @staticmethod
    def log_magic_attack(caster_name: str, target_name: str) -> None:
        """Logs a magical spell cast from the caster to the target."""
        print(f"✨ {caster_name} cast a spell on {target_name}")
    
    @staticmethod
    def log_not_enough_energy_for_attack() -> None:
        """Logs when a character doesn't have enough energy to attack."""
        print("⚠️ Not enough energy to perform the attack")
    
    @staticmethod
    def log_not_enough_mana_for_spell() -> None:
        """Logs when a character doesn't have enough mana to cast a spell."""
        print("⚠️ Not enough mana to cast the spell")
    
    @staticmethod
    def log_target_dead(character_name: str) -> None:
        """Logs that the given character has died."""
        print(f"☠️ {character_name} is dead. (x_x)")

    @staticmethod
    def log_target_already_dead(target_name: str) -> None:
        print(f"💀 {target_name} is already dead. The attack was not executed.")
    
    @staticmethod
    def log_damage_received(character_name: str, amount: int) -> None:
        """Logs the amount of damage received by a character."""
        print(f"💢 {character_name} took {amount} points of damage")
    
    @staticmethod
    def log_no_damage(character_name: str) -> None:
        """Logs when a character receives no damage."""
        print(f"🛡️  {character_name} did not receive any damage")

    @staticmethod
    def log_energy_recovered(character_name: str, amount: int) -> None:
        """Logs the energy recovery event due to rest."""
        print(f"🛌 {character_name} rested and recovered {amount} energy points")

    @staticmethod
    def log_surrender(character_name: str) -> None:
        print(f"🏳️ {character_name} has surrendered!")
