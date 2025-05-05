from action_status import ActionStatus
from character import Character
from battle_logger import BattleLogger


class BattleController:
    """
    Controls the core logic of the battle between two characters.

    This class is responsible for managing combat phases, determining the outcome 
    of actions, checking game-over conditions, and interacting with the BattleLogger
    to record significant battle events.
    """

    def __init__(self, player: Character, cpu: Character) -> None:
        """
        Initialize the battle controller with player and CPU characters.

        :param player: The player's character instance.
        :param cpu: The CPU-controlled character instance.
        """
        self.player = player
        self.cpu = cpu
    
    def is_over(self) -> bool:
        """
        Check if the battle is over.

        :return: True if either character is no longer alive, False otherwise.
        """
        return (not self.player.is_alive()) or (not self.cpu.is_alive())
    
    def get_winner(self) -> Character:
        """
        Determine and return the winner of the battle.

        :return: The character that is still alive.
        """
        if self.player.is_alive():
            return self.player
        if self.cpu.is_alive():
            return self.cpu
    
    def handle_attack(self, attacker: Character, target: Character, attacker_label: str, target_label: str) -> None:
        """
        Process an attack from one character to another, log the result.

        If the target is already dead, logs that no action is taken. If energy is 
        insufficient, or if no damage is dealt, logs those outcomes. Otherwise, 
        applies damage and logs accordingly.

        :param attacker: The character performing the attack.
        :param target: The character receiving the attack.
        :param attacker_label: Display name of the attacker for logging.
        :param target_label: Display name of the target for logging.
        """
        if not target.is_alive():
            BattleLogger.log_target_already_dead(target_label)
            return
        
        result = attacker.perform_attack(target)
        if result == ActionStatus.INSUFFICIENT_ENERGY:
            BattleLogger.log_not_enough_energy_for_attack()
            return
        if result == ActionStatus.NO_DAMAGE_RECEIVED:
            BattleLogger.log_no_damage(target_label)
            return
        
        BattleLogger.log_attack(attacker_label, target_label)
        BattleLogger.log_damage_received(target_label, result)
        if not target.is_alive():
            BattleLogger.log_target_dead(target_label)

    def execute_combat_phase(self) -> None:
        """
        Execute one turn of combat where both characters attack each other.

        The player attacks first, followed by the CPU (if both are alive).
        """
        self.handle_attack(self.player, self.cpu, self.player.name, self.cpu.name)
        self.handle_attack(self.cpu, self.player, self.cpu.name, self.player.name)
