from core.character import Character
from core.mage import Mage
from core.warrior import Warrior
from controller.battle_controller import BattleController
from session.battle_session import BattleSession


def main() -> None:
    player: Warrior = Warrior("HERO")
    cpu: Mage = Mage("VILLIAN")

    controller: BattleController = BattleController(player, cpu)
    session: BattleSession = BattleSession(controller)

    winner: Character = session.run()
    print(f"The winner is: {winner.name}")

main()