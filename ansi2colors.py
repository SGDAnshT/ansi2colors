from pathlib import Path

from parser import parse

# Read file

text = Path("logo.ansi").read_text(encoding="utf-8")

# Parse

tokens = parse(text)

print(tokens[:10])