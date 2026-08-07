# Imports
from pathlib import Path
import re

# Constants
ansi_file = Path("logo.ansi")

# Read file
data = ansi_file.read_text(encoding="utf-8")

# Regex
pattern = re.compile(
    r"\x1b\[38;2;(\d+);(\d+);(\d+)m(.)",
    re.DOTALL
)

matches = list(pattern.finditer(data))

# Palette
PALETTE = {
    "Colors.BLACK": (0, 0, 0),
    "Colors.RED": (205, 49, 49),
    "Colors.GREEN": (13, 188, 121),
    "Colors.YELLOW": (229, 229, 16),
    "Colors.BLUE": (36, 114, 200),
    "Colors.MAGENTA": (188, 63, 188),
    "Colors.CYAN": (17, 168, 205),
    "Colors.WHITE": (229, 229, 229),

    "Colors.BRIGHT_BLACK": (102, 102, 102),
    "Colors.BRIGHT_RED": (241, 76, 76),
    "Colors.BRIGHT_GREEN": (35, 209, 139),
    "Colors.BRIGHT_YELLOW": (245, 245, 67),
    "Colors.BRIGHT_BLUE": (59, 142, 234),
    "Colors.BRIGHT_MAGENTA": (214, 112, 214),
    "Colors.BRIGHT_CYAN": (41, 184, 219),
    "Colors.BRIGHT_WHITE": (255, 255, 255),
}

# Functions
def distance(c1, c2):
    return sum(
        (a-b)**2
        for a, b in zip(c1, c2)
    )

def nearest(rgb):
    best = None
    best_distance = float("inf")

    for name, color in PALETTE.items():
        d = distance(rgb, color)

        if d < best_distance:
            best = name
            best_distance = d

    return best

for match in matches[:20]:

    rgb = (
        int(match.group(1)),
        int(match.group(2)),
        int(match.group(3)),
    )

    ch = match.group(4)

    print(rgb, repr(ch))