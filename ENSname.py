import requests




BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def colour_print(text: str, *effects: str) -> None:
    """
    Print `text` using the ANSI sequences to change colour, etc

    :param text: The text to print.
    :param effects: The effect we want.  One of the constants
        defined at the start of this module.
    """
    effect_string = "".join(effects)
    output_string = "{0}{1}{2}".format(effect_string, text, RESET)
    print(output_string)


def naughty_request(website: str):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                             "(KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
    r = requests.get(website, headers=headers)
    r = r.text
    r = str(r)
    return r



words = ['lorimer', 'ben', 'jane']




for word in words:
    req = naughty_request("https://etherscan.io/enslookup-search?search={}.eth".format(word))
    found = 0
    for index, i in enumerate(req):
        if i == "i":
            if req[index:index + 27] == "is not currently registered":
                colour_print("{} hasn't been registered".format(word.upper()), GREEN)
                found = 1
                break
    if found == 0:
        print("{} has been registered".format(word.upper()))
        found = 1
