import argparse

VALID_SMOOTH_MODES = {"rgb", "len", "all"}

def parse_args():
    parser = argparse.ArgumentParser(
        prog="ansi2colors",
        description="Convert ANSI-colored ASCII art into optimized Python source."
    )

    parser.add_argument(
        "input",
        help="Input ANSI file."
    )

    parser.add_argument(
        "--smooth",
        metavar="MODE",
        help="Enable smoothing: rgb, len, rgb,len, or all."
    )

    return parser.parse_args()


def get_smoothing_modes(value):
    if value is None:
        return set()

    if value == "all":
        return {"rgb", "len"}

    modes = {
        mode.strip()
        for mode in value.split(",")
    }

    invalid = modes - {"rgb", "len"}

    if invalid:
        raise ValueError(
            f"Invalid smoothing mode(s): {', '.join(sorted(invalid))}"
        )

    return modes