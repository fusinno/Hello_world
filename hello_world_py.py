"""Generate colored ASCII art for 'Hello World!'"""

import random

import pyfiglet
from colorama import Fore, Style, init


def hello_world_word_art() -> None:
    """Print a colorful 'Hello World!' using pyfiglet with random colors."""

    # Initialize colorama to ensure ANSI codes work on all platforms
    init(autoreset=True)

    # Create ASCII art with a more stylish font
    ascii_art = pyfiglet.figlet_format("Hello World!", font="slant")

    # Define a palette of colors to choose from
    colors = [
        Fore.RED,
        Fore.GREEN,
        Fore.YELLOW,
        Fore.BLUE,
        Fore.MAGENTA,
        Fore.CYAN,
        Fore.WHITE,
    ]

    # Color each character individually with a random color
    colored_chars = []
    for char in ascii_art:
        if char.strip():
            colored_chars.append(random.choice(colors) + char + Style.RESET_ALL)
        else:
            colored_chars.append(char)

    print("".join(colored_chars))


if __name__ == "__main__":
    hello_world_word_art()
