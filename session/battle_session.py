from core.battle_logger import BattleLogger
from view.battle_view import BattleView
from controller.battle_controller import BattleController
from core.character import Character


class BattleSession:
    """
    Manages the flow of the battle between the player and the CPU.

    Responsible for handling user input, processing game options, and 
    delegating combat logic to the BattleController. It serves as the 
    main game loop for the battle system.
    """

    def __init__(self, controller: BattleController) -> None:
        """
        Initialize the battle session with a BattleController.

        :param controller: Instance of BattleController managing the characters and combat.
        """
        self.controller = controller

    def run(self) -> Character:
        """
        Run the main battle loop until one character is defeated.

        Presents battle options to the user each turn, processes the selected 
        action, and executes the CPU’s response if appropriate. Clears the 
        screen between turns and waits for user input.

        :return: The winning character at the end of the battle.
        """
        turn: int = 0

        while not self.controller.is_over():
            BattleView.show_battle_options()
            option = BattleView.request_user_option()

            if self.controller.player.is_alive():
                self.process_option(option)
                if option == "1":
                    turn += 1

            input("Press Enter to continue...")
            BattleView.clear_screen()

        return self.controller.get_winner()

    def process_option(self, option: str) -> None:
        """
        Process the player's selected action.

        Handles attacking, recovering energy, showing character stats,
        or surrendering. Logs appropriate messages for energy recovery.

        :param option: String representing the player's menu choice.
        """
        if option == "1":
            self.controller.execute_combat_phase()
        elif option == "2":
            self.controller.player.recover_energy()
            BattleLogger.log_energy_recovered(self.controller.player.name, amount=20)
        elif option == "3":
            BattleView.show_character_stats(self.controller.player)
        elif option == "4":
            BattleView.show_character_stats(self.controller.cpu)
        elif option == "5":
            pass  # Placeholder for surrender logic (to be implemented)
