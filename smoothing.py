from tokens import Token

from palette import rgb_distance

def smooth_tokens(tokens):
    for i in range(1, len(tokens) - 1):
        prev = tokens[i - 1]
        current = tokens[i]
        next = tokens[i + 1]