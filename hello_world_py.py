import pyfiglet

def hello_world_word_art():
    ascii_art = pyfiglet.figlet_format("Hello World!")
    print(ascii_art)

if __name__ == "__main__":
    hello_world_word_art()