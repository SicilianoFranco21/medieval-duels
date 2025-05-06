from core.mage import Mage
from core.warrior import Warrior
from session.battle_session import BattleSession
from controller.battle_controller import BattleController


class MainController:    
    @staticmethod
    def start_new_battle() -> None:
        hero = MainController.create_new_player("HERO", "warrior")
        villian = MainController.create_new_player("VILLIAN", "mage")
        controller: BattleController = BattleController(hero, villian)
        battle_session: BattleSession = BattleSession(controller)
        battle_session.run()
        
    @staticmethod
    def load_player() -> None:
        pass
    
    @staticmethod
    def create_new_player(name: str, class_name: str) -> Mage | Warrior:
        if class_name.lower() == "warrior":
            return Warrior(name)
        elif class_name.lower() == "mage":
            return Mage(name)