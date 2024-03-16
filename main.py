from tkinter import *
from tkinter import messagebox
from random import randint
from time import sleep


app_title = "Simple App"
label = "Are you gay?"
yes_message = "Ayo! I knew it!"
no_message = "Well done! Bye bye!"


def yes_handler() -> None:
    messagebox.showinfo('', yes_message)
    quit()


def no_handler() -> None:
    messagebox.showinfo('', no_message)
    quit()


def no_moving_handler(event) -> None:
    button_no.place(x=randint(0, 500), y=randint(0, 500))
    sleep(0.1)


if __name__ == "__main__":
    root = Tk()
    root.geometry("600x600")
    root.title(app_title)
    root.resizable(width=False, height=False)
    root['bg'] = 'black'

    Label(root, text=label, font="Arial 20 bold", bg='black', fg='white').pack()

    button_yes = Button(root, text="Yes", font="Arial 20 bold", command=yes_handler)
    button_yes.place(x=170, y=100)

    button_no = Button(root, text="No", font="Arial 20 bold", command=no_handler)
    button_no.place(x=350, y=100)
    button_no.bind("<Enter>", no_moving_handler)

    root.mainloop()
