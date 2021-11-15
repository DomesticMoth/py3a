import enum
from .errors import *

class ConvertableEnum(enum.Enum):
    @classmethod
    def _error_type(cls):
        return ValueError

    def __str__(self) -> str:
        return str(self.value)
    
    @classmethod
    def fromstr(cls, s: str):
        for k, v in cls.__members__.items():
            if str(v) == str(s):
                return cls[k]
        else:
            raise cls._error_type()(f"'{cls.__name__}' enum not found for '{s}'")

class ColorMod(ConvertableEnum):
    none = 'none'
    fg = 'fg'
    bg = 'bg'
    full = 'full'

    @classmethod
    def _error_type(cls):
        return UnknownColorMod

    def to_datacols(self) -> int:
        if self.value == 'none':
            return 1
        elif self.value == 'fg':
            return 2
        elif self.value == 'bg':
            return 2
        elif self.value == 'full':
            return 3

class Color(ConvertableEnum):
    BLACK = '0'
    BLUE = '1'
    GREEN = '2'
    CYAN = '3'
    RED = '4'
    MAGENTA = '5'
    YELLOW = '6'
    WHITE = '7'
    GRAY = '8'
    BRIGHT_BLUE = '9'
    BRIGHT_GREEN = 'a'
    BRIGHT_CYAN = 'b'
    BRIGHT_RED = 'c'
    BRIGHT_MAGENTA = 'd'
    BRIGHT_YELLOW = 'e'
    BRIGHT_WHITE = 'f'
    
    @classmethod
    def _error_type(cls):
        return UnknownColor
