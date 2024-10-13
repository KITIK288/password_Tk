# Это программа для создания пароля в окне питон тк

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

def pas_gen():

    password = ""
    nums_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sim_list =  ["а", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
    "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E","F", "G", "H", "I", "J", "K", "L", "M", "N",
    "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "!","#","$","%","&","'","(",")","*","+",
    "-",".","/",";",":","<","=",">","?","@","[","]","^","_","`","{","|","}","~"
    ]

    first_counter = 0
    second_counter = 0
    while 1:
        sim_element = random.choice(sim_list)
        password = password + sim_element
        first_counter += 1
        if first_counter == 10:
            break
    while 1:
        num_element = random.choice(nums_list)
        num_element = str(num_element)
        password = password + num_element
        second_counter += 1
        if second_counter == 3:
            break

    messagebox.showinfo("Пароль сгенрирован", password)


root = Tk()
root.title("Программа для создания пароля")
root.geometry("400x200")

l1 = Label(text='Программа для создания пароля', font='Arial 20')
l1.pack()

btn = ttk.Button(text="Сгенерировать пароль", command=pas_gen, width=30)
btn.pack()

root.mainloop()
