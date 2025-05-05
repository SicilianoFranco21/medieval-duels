from character import Character
from mage import Mage
from warrior import Warrior
from battle_controller import BattleController
from battle_session import BattleSession


def main() -> None:
    player: Warrior = Warrior("HERO")
    cpu: Mage = Mage("VILLIAN")

    controller: BattleController = BattleController(player, cpu)
    session: BattleSession = BattleSession(controller)

    winner: Character = session.run()
    print(f"The winner is: {winner.name}")

main()