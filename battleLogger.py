class BattleLogger:
    @staticmethod
    def log_attack(attacker_name: str, target_name: str) -> None:
        print(f"{attacker_name} performed an attack on {target_name}")
    
    @staticmethod
    def log_not_enough_energy() -> None:
        print("Not enough energy to perform the attack")
    
    @staticmethod
    def log_target_dead(target_name: str) -> None:
        print(f"{target_name} is dead. (x_x)")
    
    @staticmethod
    def log_damage_received(character_name: str, damage: int) -> None:
        print(f"{character_name} took {damage} points of damage")
    
    @staticmethod
    def log_no_damage(character_name: str) -> None:
        print(f"{character_name} did not receive any damage")