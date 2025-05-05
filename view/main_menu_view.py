from view.base_view import BaseView


class MainMenuView(BaseView):
    """
    A class responsible for displaying and handling the main menu
    in the Medieval Duels game.

    This view presents the user with the primary navigation options,
    such as starting a battle, loading a saved player, creating a new
    player, or exiting the game.

    All methods are static since no instance state is required.
    """

    @staticmethod
    def show_main_menu() -> None:
        """
        Displays the main menu options to the user.

        The menu includes:
        1. Start New Battle
        2. Load Player
        3. Create New Player
        4. Exit
        """
        print("=" * 40)
        print("⚔️  MEDIEVAL DUELS ⚔️".center(40))
        print("=" * 40)
        print("1. Start New Battle")
        print("2. Load Player")
        print("3. Create New Player")
        print("4. Exit")
        print("=" * 40)
