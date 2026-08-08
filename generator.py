def group_tokens(tokens):
    if not tokens:
        return []
    groups = []

    current_color = tokens[0].color
    current_text = ""

    for token in tokens:
        if token.color == current_color:
            current_text += token.text

        else:
            groups.append((current_color, current_text))

            current_color = token.color
            current_text = token.text

    groups.append((current_color, current_text))

    return groups