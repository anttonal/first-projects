import tkinter as tk
import random as rd

root = tk.Tk()

mainFrame = tk.Frame(master=root)
mainFrame.grid()


def destroy(event):
    event.widget.destroy()


for i in range(10):
    mainFrame.columnconfigure(i, minsize=50, weight=1)
    mainFrame.rowconfigure(1, minsize=50, weight=1)

    for j in range(1):
        frameNumbers = tk.Frame(master=mainFrame)
        frameNumbers.grid(column=i, row=j)

        btnRandNumbers = rd.randint(0, 100)

        btnNumber = tk.Button(master=frameNumbers,
                              text=btnRandNumbers)  # command would lead to another function in my main program, not really relevant
        btnNumber.bind('<ButtonRelease-1>', destroy)
        btnNumber.grid()