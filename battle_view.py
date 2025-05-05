from character import Character


class BattleView:
    @staticmethod
    def show_battle_options() -> None:
        print("+=====================================+")
        print("|         🧭 BATTLE OPTIONS            |")
        print("+-------------------------------------+")
        print("| 1. ⚔️  Attack                        |")
        print("| 2. 🔋 Recover Energy                 |")
        print("| 3. 📊 Show Player Status             |")
        print("+=====================================+")

    @staticmethod
    def request_user_option() -> str:
        option: str = input("Enter an option: ")
        return option
    
    @staticmethod
    def show_character_stats(character: Character) -> None:
        print("\n" + "=" * 40)
        print(f" 📛  {character.name.upper()}")
        print("=" * 40)

        print(f" ❤️  Vida:   {character.health}")
        print(f" ⚡ Energía: {character.energy}")
        print(f" 🗡️  Ataque:  {character.attack}")
        print(f" 🛡️  Defensa: {character.defense}")
        print("=" * 40)