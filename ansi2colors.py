from pathlib import Path

from parser import parse

from generator import group_tokens

# Read file

text = Path("logo.ansi").read_text(encoding="utf-8")

# Parse

tokens = parse(text)

groups = group_tokens(tokens)

print(groups[:20])