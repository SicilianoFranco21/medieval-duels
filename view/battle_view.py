from core.character import Character
from view.base_view import BaseView



class BattleView(BaseView):
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
    def show_character_stats(character: Character) -> None:
        print("=" * 40)
        print(f" 📛  {character.name.upper()}")
        print("=" * 40)

        print(f" ❤️  Vida:   {character.health}")
        print(f" ⚡ Energía: {character.energy}")
        print(f" 🗡️  Ataque:  {character.attack}")
        print(f" 🛡️  Defensa: {character.defense}")
        print("=" * 40)