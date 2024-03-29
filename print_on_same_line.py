from time import sleep
import sys

BLINK = 0.2
chars_in_line = 10

def open_file(fn):
    with open(fn, "r") as f:
        for line in f:
            if line:
                yield line

def type_out_text_to_line(text, end="", sep="", line_chars=None, blink=0.2):
    if not text:
        return ""

    c = line_chars
    for i, j in enumerate(text):
        sleep(blink)
        print(j, end=end, sep=sep, flush=True)
        if line_chars:
            if i + 1 == c:
                print()
                c += line_chars
    return ""

print("\n\tSTART PRINTING\n")

for text in open_file('example.txt'):
    if len(text) > 1:
        print(type_out_text_to_line(text, line_chars=chars_in_line, blink=BLINK, sep=""))
print("\n\tEND PRINTING\n")
