from tkinter import *
import ctypes
import re

# Increas Dots Per inch so it looks sharper
ctypes.windll.shcore.SetProcessDpiAwareness(True)

root = Tk()
root.geometry('700x700')

previousText = ''

# Define colors for the variouse types of tokens
normal = "#EAEAEA"
keywords = "#EA5F5F"
comments = "#5FEAA5"
string = "#EAA25F"
variables = "#3681c6"
background = "#2A2A2A"
font = 'Consolas 15'

s = {"a":"" , "b": ""}

list = []

for key in s :
    list.append(key)
txt = " | ".join(list)
print(txt)


# Define a list of Regex Pattern that should be colored in a certain way
repl = [
    ['(^| )(False|None|True|and|as|assert|async|await|break|class|continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)($| )', keywords],
    ['".*?"', string],
    ['\'.*?\'', string],
    ['#.*?$', string],
    [txt , variables ],
    ['^\s*(\w+)\s*\((.*)\)\s*$' , comments]
]
editArea = Text(
    root,
    background=background,
    foreground=normal,
    insertbackground=normal,
    relief=FLAT,
    borderwidth=30,
    font=font
)
editArea.pack(
    fill=BOTH,
    expand=1
)

# Insert some Standard Text into the Edit Area
editArea.insert('1.0', """from argparse import ArgumentParser
from random import shuffle, choice
import string

# Setting up the Argument Parser
parser = ArgumentParser(

    prog='Password Generator.',
    description='Generate any number of passwords with this tool.'
)
""")
list = ["amigo" , "ami"]


def search_re(pattern, text):
    matches = []
    text = text.splitlines()
    for i, line in enumerate(text):
        for match in re.finditer(pattern, line):

            matches.append(
                (f"{i + 1}.{match.start()}", f"{i + 1}.{match.end()}")
            )

    return matches

def changes(event=None):
    for tag in editArea.tag_names():
        editArea.tag_remove(tag, "1.0", "end")
        # Add tags where the search_re variables found the pattern
    i = 0
    for pattern, color in repl:
        for start, end in search_re(pattern, editArea.get('1.0', END)):
            editArea.tag_add(f'{i}', start, end)
            editArea.tag_config(f'{i}', foreground=color)
            i+=1

editArea.bind('<KeyRelease>', changes)

changes()
root.mainloop()
