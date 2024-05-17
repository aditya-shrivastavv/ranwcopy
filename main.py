from wonderwords import RandomWord, RandomSentence
import pyperclip
import random
import time
import sys
import winsound
from constants import const

rw = RandomWord()
rs = RandomSentence()

if len(sys.argv) == 2:
    const.iterations = int(sys.argv[1])

for i in range(const.iterations):
    balancer = round(random.random())

    if balancer:
        word = rw.word()
        pyperclip.copy(word)
    else:
        sentence = rs.simple_sentence()
        pyperclip.copy(sentence)

    for remaining in range(const.timegap, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write(f"{remaining} seconds remaining")
        sys.stdout.flush()
        time.sleep(1)

    sys.stdout.write("\rPaste!!!                  \n")
    winsound.Beep(const.sound_frequency, const.sound_duration)
    print("Iterations remaining: ", const.iterations - i - 1, "\n")
