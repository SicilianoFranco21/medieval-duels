from core.character import Character
from view.base_view import BaseView

class BattleView(BaseView):
    """
    Displays the battle interface for the Medieval Duels game.

    This class handles the battle menu and the display of character stats
    during the fight.
    """

    @staticmethod
    def show_battle_options() -> None:
        """
        Displays the available actions the player can take during battle.

        The options include:
        1. Attack
        2. Recover Energy
        3. Show Player Status
        4. Show CPU Status
        5. Surrender
        """
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
    def show_character_stats(character: Character) -> None:
        """
        Displays the current stats of a character in a structured format.

        Args:
            character (Character): The character whose stats will be shown.
        """
        print("=" * 40)
        print(f" 📛  {character.name.upper()}")
        print("=" * 40)

        print(f" ❤️  Vida:   {character.health}")
        print(f" ⚡ Energía: {character.energy}")
        print(f" 🗡️  Ataque:  {character.attack}")
        print(f" 🛡️  Defensa: {character.defense}")
        print("=" * 40)