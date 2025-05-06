from controller.battle_controller import BattleController
from session.battle_session import BattleSession
from controller.main_controller import MainController
from view.main_menu_view import MainMenuView


class MainSession:
    def __init__(self):
        self.running: bool = True
    
    def process_option(self, option: str) -> None:
        if option == "1":
            MainController.start_new_battle()
        elif option == "2":
            pass
        elif option == "3":
            pass
        elif option == "4":
            print("Hasta luego")
            self.running = False

    
    def run(self) -> None:
        while self.running:
            MainMenuView.show_main_menu()
            option: str = MainMenuView.request_user_option()
            MainMenuView.clear_screen()

            self.process_option(option)
            if self.running and option != "1":
                MainMenuView.wait_for_user()
                MainMenuView.clear_screen()
            
