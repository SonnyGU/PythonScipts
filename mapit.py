#! python3
import pyperclip
import sys
import webbrowser


# if arguments were passed
if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/" + address)
