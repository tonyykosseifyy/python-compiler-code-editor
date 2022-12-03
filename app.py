import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.ttk import *

def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")

def save_file():
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")

window = tk.Tk()
window.title("TK Text Editor")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

style = Style()
 
style.configure('TButton', font =
               ('calibri', 16, 'bold'),
                    borderwidth = '4')
style.configure('TFrame', background='#2A2A2A')

style.map('TButton')

txt_edit = tk.Text(window)
frm_buttons = Frame(window, relief=tk.RAISED ,borderwidth=2, width=400 )
btn_open = Button(frm_buttons, text="Open", command=open_file)
btn_save = Button(frm_buttons, text="Save As...", command=save_file)
btn_run = Button(frm_buttons, text="Run")

##image = "image.png", compound=LEFT

btn_open.grid(row=0, column=0, sticky="ew", padx=15, pady=30)
btn_save.grid(row=1, column=0, sticky="ew", padx=15)
btn_run.grid(row=2, column=0, sticky="ew", padx=15, pady=30,)


frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")


window.mainloop()