from enum import IntEnum

class ActionStatus(IntEnum):
    INSUFFICIENT_ENERGY = 0
    INSUFFICIENT_MANA = -1
    SUCCESS = 1