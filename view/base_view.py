from abc import ABC
from os import system as os_system
from platform import system as platform_system


class BaseView(ABC):
    @staticmethod
    def request_user_option() -> str:
        option: str = input("Enter an option: ")
        return option

    @staticmethod
    def clear_screen() -> None:
        if platform_system() == "Windows":
            os_system("cls")
        else:
            os_system("clear")

    @staticmethod
    def wait_for_user() -> None:
        """
        Pause the program execution until the user presses Enter.

        This method is typically used to allow the player to read messages 
        or battle outcomes before the screen is cleared or the game proceeds 
        to the next action.
        """
        input("Press Enter to continue...")