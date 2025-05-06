from core.character import Character
from core.mage import Mage
from core.warrior import Warrior
from controller.battle_controller import BattleController
from session.battle_session import BattleSession
from session.main_session import MainSession


def main() -> None:
    session: MainSession = MainSession()
    session.run()
main()