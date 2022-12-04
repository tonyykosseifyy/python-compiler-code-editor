import tkinter as tk
import tkinter.scrolledtext as tkscrolled
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.ttk import *
import ctypes
import re
from main import * 
from test import convertTabToIndent
# Increas Dots Per inch so it looks sharper
ctypes.windll.shcore.SetProcessDpiAwareness(True)

window = tk.Tk()
window.title("TK Code Editor")

window.rowconfigure(1, minsize=500, weight=1)
window.columnconfigure(1, minsize=500, weight=1)

style = Style()
style.configure('TButton', font =
               ('calibri', 16, 'bold'),
                    borderwidth = '4')
style.configure('TFrame', background='#2A2A2A')
style.map('TButton')

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
errors = []


editArea = tk.Text(
    window,
    background=background,
    foreground=normal,
    insertbackground=normal,
    font=font,
    padx=5,
    pady=15
)


def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    editArea.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        editArea.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")

def save_file():
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = editArea.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"TK Code Editor - {filepath}")


frm_buttons = Frame(window,borderwidth=1, width=400 )
btn_open = Button(frm_buttons, text="Open", command=open_file)
btn_save = Button(frm_buttons, text="Save As...", command=save_file)
btn_run = Button(frm_buttons, text="Run")

output_area = tk.Frame(window, height=600, borderwidth=2 , relief=tk.RAISED, background="#2A2A2A")
output_area.grid(row=1 , column=1,columnspan=2, sticky="nsew")

output_lbl = Label(output_area, text="Output" , foreground="white", background="#2A2A2A")
output_lbl.pack(side="top")


output_text = tk.Text(output_area,font=font, foreground="red" , background="#2A2A2A")
scrollbar = Scrollbar(output_area, command=output_text.yview)


scrollbar.pack(side='right', fill='y')

output_text.pack(fill=tk.BOTH)


btn_open.grid(row=0, column=0, sticky="ew", padx=15, pady=30)
btn_save.grid(row=1, column=0, sticky="ew", padx=15)
btn_run.grid(row=2, column=0, sticky="ew", padx=15, pady=30,)


frm_buttons.grid(row=0, column=0, sticky="ns", rowspan=2)
editArea.grid(row=0, column=1, sticky="nsew")

previousText = ''

# Define a list of Regex Pattern that should be colored in a certain way
repl = [
    ['(^| )(False|None|True|and|as|assert|async|await|break|class|continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)($| )', keywords],
    ['".*?"', string],
    ['\'.*?\'', string],
    ['#.*?$', string],
    [txt , variables ],
    ['^\s*(\w+)\s*\((.*)\)\s*$' , comments]
]


# Insert some Standard Text into the Edit Area
##editArea.insert('1.0', "a = b")


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
        for start, end in search_re(pattern, editArea.get('1.0', tk.END)):
            editArea.tag_add(f'{i}', start, end)
            editArea.tag_config(f'{i}', foreground=color)
            i+=1
    tagErrors()
    outputErrors()

def tagErrors(event=None) :
    for i in range(len(errors)) :
        if errors[i] != None and errors[i] != True :
            editArea.tag_add("highlitline", f'{i+1}.0', f'{i+2}.0')
            editArea.tag_config("highlitline", background="red", foreground="white")

def outputErrors(event=None):
    output_text.config(state="normal")
    output_text.delete("1.0","end")
    errors_text = ""
    for i in range(len(errors)) :
        if errors[i] != None and errors[i] != True :
            errors_text+=f'{i+1} - {errors[i]}\n' 
    
    output_text.insert("1.0" , errors_text)
    output_text.config(state="disabled") 

def run(event=None) :
    line_text = editArea.get(1.0,tk.END)
    line_text = line_text.split("\n")
    errors.clear()
    line_text.pop(-1)
    indentation["indent"] = 0 
    indentation["required"] = False 
    indentation["block"] = "none"
    Line.line_count = 1
    print("line text", line_text)
    for line in range(len(line_text)) :
        print(indentation)
        if len(line_text[line]) == 0 and line_text[line] == "":
            errors.append(None)
            Line.line_count +=1  
        else : errors.append(Line(convertTabToIndent(line_text[line])).check())
    print("errors",  errors)

editArea.bind('<KeyRelease>', changes)
editArea.bind("<Return>" , run )

window.mainloop()