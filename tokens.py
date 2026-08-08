from dataclasses import dataclass

@dataclass
class Token:
    color: str
    text: str
    rgb: tuple[int, int, int]