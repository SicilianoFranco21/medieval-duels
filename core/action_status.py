from enum import IntEnum

class ActionStatus(IntEnum):
    INSUFFICIENT_ENERGY: int = 0
    SUCCESS: int = -1
    INSUFFICIENT_MANA: int = -2
    NO_DAMAGE_RECEIVED: int = -3
    