from dataclasses import dataclass

@dataclass
class Token:
    color: str
    char: str
    rgb: tuple[int, int, int]