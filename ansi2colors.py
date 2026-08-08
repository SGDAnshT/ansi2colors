from pathlib import Path

from cli import parse_args, get_smoothing_modes

from parser import parse

from generator import group_tokens

from smoothing import smooth_tokens

# Read file

text = Path("logo.ansi").read_text(encoding="utf-8")

# Parse

tokens = smooth_tokens(parse(text))

groups = group_tokens(tokens)

args = parse_args()

try:
    smooth_modes = get_smoothing_modes(args.smooth)
except ValueError as e:
    print(e)
    exit(1)

print(smooth_modes)