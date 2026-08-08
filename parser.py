import re
from palette import nearest
from tokens import Token


PATTERN = re.compile(
    r"\x1b\[38;2;(\d+);(\d+);(\d+)m(.)",
    re.DOTALL,
)

def parse(text):
    tokens = []
    for match in PATTERN.finditer(text):
        rgb = (
            int(match.group(1)),
            int(match.group(2)),
            int(match.group(3)),
        )

        char = match.group(4)

        color = nearest(rgb)

        tokens.append(
            Token(color, char)
        )

    return tokens