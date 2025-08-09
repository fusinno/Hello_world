"""Generate colored ASCII art for 'Hello World!'"""

import pyfiglet
from colorama import Fore, Style, init


def hello_world_word_art() -> None:
    """Print a colorful 'Hello World!' using pyfiglet."""

    # Initialize colorama to ensure ANSI codes work on all platforms
    init(autoreset=True)

    # Create ASCII art with a more stylish font
    ascii_art = pyfiglet.figlet_format("Hello World!", font="slant")

    # Apply cyan color to the ASCII art
    colored_art = f"{Fore.CYAN}{ascii_art}{Style.RESET_ALL}"

    print(colored_art)


if __name__ == "__main__":
    hello_world_word_art()
