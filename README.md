# ⚔️ Medieval Duels

**Medieval Duels** is a turn-based console game where two characters — a hero and a villain — face off in strategic battles. Each character can be a **Warrior** or a **Mage**, with different abilities, and must make tactical decisions to defeat their opponent.

## 🗂️ Project Structure

```
medieval-duels/
├── core/
│   ├── action_status.py                    # Enum of available actions
│   ├── character.py                        # Definition of the Character class and subclasses
│   ├── logger.py                           # Battle event logger
├── controller/
│   ├── battle_controller.py                # Battle logic
│   ├── main_controller.py                  # Main game coordination
├── session/
│   ├── battle_session.py                   # Handles battle sessions
│   ├── main_session.py                     # Manages main sessions
├── tests/
│   ├── utils/               
│   │    ├── pretty_summary_formatter.py    # Formats test summaries with readable output
│   │    └── pretty_test_result.py          # Custom result class to enhance unittest output
│   ├── test_mage.py                        # Unit tests for the Mage class
│   ├── test_warrior.py                     # Unit tests for the Warrior class
├── view/
│   ├── base_view.py                        # Base class for views
│   ├── battle_view.py                      # Battle view
│   ├── main_menu_view.py                   # Main menu view
├── main.py                                 # Game entry point
├── run_tests.py                            # Script to run tests
└── README.md
```

## 🧙 Characters

- **Warrior**: High defense and physical attack.
- **Mage**: Lower defense, but powerful magic attacks and good energy recovery.

## 🎮 How to Play

1. Run the main file:

```
python main.py
```

2. From the main menu, you can:
   - Start a new battle
   - Load an existing player
   - Create a new player
   - Exit the game

3. During battle, you can:
   - Attack
   - Recover energy
   - View player or CPU status
   - Surrender

## ✅ Requirements

- Python 3.8+
- No external libraries required

## 🔍 Tests

To run the available tests:

```
python run_tests.py
```

## 📌 Status

This project is under development. Future improvements may include:
- Save/load system
- Improved AI
- Special abilities
- Leveling and progression system

## 👤 Author

- **Created by:** SicilianoFranco21
- **Linkedin:** [Franco Siciliano](https://www.linkedin.com/in/franco-siciliano/)

---

Get ready for the medieval duel!
