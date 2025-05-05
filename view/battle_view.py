from core.character import Character
from os import system as os_system
from platform import system as platform_system


class BattleView:
    @staticmethod
    def show_battle_options() -> None:
        print("+=====================================+")
        print("|         ⚔️  BATTLE OPTIONS           |")
        print("+-------------------------------------+")
        print("| 1. 🗡️  Attack                        |")
        print("| 2. 💧 Recover Energy                |")
        print("| 3. 🧍 Show Player Status            |")
        print("| 4. 🤖 Show CPU Status               |")
        print("| 5. 🏳️  Surrender                     |")
        print("+=====================================+")

    @staticmethod
    def request_user_option() -> str:
        option: str = input("Enter an option: ")
        return option
    
    @staticmethod
    def show_character_stats(character: Character) -> None:
        print("=" * 40)
        print(f" 📛  {character.name.upper()}")
        print("=" * 40)

        print(f" ❤️  Vida:   {character.health}")
        print(f" ⚡ Energía: {character.energy}")
        print(f" 🗡️  Ataque:  {character.attack}")
        print(f" 🛡️  Defensa: {character.defense}")
        print("=" * 40)

    @staticmethod
    def wait_for_user() -> None:
        """
        Pause the program execution until the user presses Enter.

        This method is typically used to allow the player to read messages 
        or battle outcomes before the screen is cleared or the game proceeds 
        to the next action.
        """
        input("Press Enter to continue...")

    @staticmethod
    def clear_screen() -> None:
        if platform_system() == "Windows":
            os_system("cls")
        else:
            os_system("clear")