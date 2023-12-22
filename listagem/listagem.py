
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Label, Listbox, StringVar, Tk, Canvas, Entry, Button, PhotoImage, Scrollbar, END, messagebox
import numpy


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Users\20221041110019\Documents\python\projeto-final-Peoo\listagem\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


Listagem = Tk()

Listagem.geometry("350x450")
Listagem.configure(bg = "#343034")
Listagem.title("listagem")

global num
num = StringVar()
scrollbar = Scrollbar()
Screen = StringVar()
lista = []
minor = False
average = False
bigger = False

def inserir_num():

    entry_2.delete(0, END)
    lista.append(float(num.get()))

    for numero in lista:
        entry_2.insert(END, numero)
        
    num.set("")
    print(lista)

def Minor():
    global minor, average, bigger
    minor = True
    average = False
    bigger = False

def Menor():
    m = min(lista)
    return f"o menor número é: {m}"
    
def Bigger():
    global minor, average, bigger
    minor = False
    average = False
    bigger = True

def Maior():
    m = max(lista)
    return f"o maior número é: {m}"

def Average():
    global minor, average, bigger
    minor = False
    average = True
    bigger = False

def Media():
    m = sum(lista)/len(lista)
    return f"a média dos números é: {m}"

def calcular():
    dicionario = {minor:Menor(), 
              bigger:Maior(), 
              average:Media()}
    
    for option, resultado in dicionario.items():
        print(minor)
        if option:
            messagebox.showinfo(message=resultado)
            print(resultado)

canvas = Canvas(
    Listagem,
    bg = "#343034",
    height = 450,
    width = 350,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    23.0,
    54.0,
    anchor="nw",
    text="Inserir número:",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    220.0,
    67.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    textvariable=num
)
entry_1.place(
    x=159.0,
    y=59.0,
    width=122.0,
    height=15.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: inserir_num(),
    relief="flat"
)
button_1.place(
    x=288.0,
    y=60.0,
    width=44.0,
    height=16.0
)

# canvas.create_rectangle(
#     23.0,
#     103.0,
#     325.0,
#     364.0,
#     fill="#D9D9D9",
#     outline="")

entry_2 = Listbox(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    yscrollcommand=scrollbar
)

entry_2.place(
    x=33.0,
    y=117.0,
    width=281.0,
    height=250
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Minor(),
    relief="flat"
)
button_2.place(
    x=73.0,
    y=384.0,
    width=22.0,
    height=22.0
)

canvas.create_text(
    101.0,
    389.0,
    anchor="nw",
    text="Menor",
    fill="#FFFFFF",
    font=("Inter", 10 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Bigger(),
    relief="flat"
)
button_3.place(
    x=146.0,
    y=384.0,
    width=22.0,
    height=22.0
)

canvas.create_text(
    174.0,
    389.0,
    anchor="nw",
    text="Maior",
    fill="#FFFFFF",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    240.0,
    389.0,
    anchor="nw",
    text="média",
    fill="#FFFFFF",
    font=("Inter", 10 * -1)
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Average(),
    relief="flat"
)
button_4.place(
    x=212.0,
    y=384.0,
    width=22.0,
    height=22.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: calcular(),
    relief="flat"
)
button_5.place(
    x=141.0,
    y=417.0,
    width=56.0,
    height=17.0
)
Listagem.resizable(False, False)
Listagem.mainloop()
