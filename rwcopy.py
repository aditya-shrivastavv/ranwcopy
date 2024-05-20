#!python
from wonderwords import RandomWord, RandomSentence
import pyperclip
import random
import time
import sys
import winsound
from argparse import ArgumentParser

SOUND_FREQUENCY = 2500
SOUND_DURATION = 400  # milli second

parser = ArgumentParser(
    prog="rwcopy",
    description="Generates random words and sentences and copyies them to the clipboard.",
    epilog="rwcopy - by Aditya Shrivastav",
)

parser.add_argument(
    "--gethelper", help="Copy Javascript console automation code", action="store_true"
)
parser.add_argument(
    "-i",
    "--iterations",
    default=10,
    help="Number of words/sentences to generate (default = 10)",
)
parser.add_argument(
    "-g",
    "--timegap",
    default=8,
    help="Time gap (sec) between word consequent word generations (default = 8)",
)
raw_args = parser.parse_args()

if raw_args.gethelper != None:
    with open("paste.js") as file:
        code = file.read()
        pyperclip.copy(code)
    print("Code copied to your clipboard.")
    sys.exit(0)

args = {}
try:
    args = {"iterations": int(raw_args.iterations), "timegap": int(raw_args.timegap)}
except ValueError:
    raise Exception("Both `iterations` and `timegap must be integer values.")

rw = RandomWord()
rs = RandomSentence()

for i in range(args["iterations"]):
    balancer = round(random.random())

    if balancer:
        word = rw.word()
        pyperclip.copy(word)
    else:
        sentence = rs.simple_sentence()
        pyperclip.copy(sentence)

    for remaining in range(args["timegap"], 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write(f"{remaining} seconds remaining")
        sys.stdout.flush()
        time.sleep(1)

    sys.stdout.write("\rPaste!!!                  \n")
    winsound.Beep(SOUND_FREQUENCY, SOUND_DURATION)
    print("Iterations remaining: ", args["iterations"] - i - 1, "\n")
