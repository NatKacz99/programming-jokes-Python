import tkinter as tk
import pyjokes

def get_joke():
    try:
        joke = pyjokes.get_joke()
        joke_label.config(text=joke)
        status_label.config(text="Joke loaded!")
    except Exception as e:
        joke_label.config(text="Error while downloading joke")
        status_label.config(text="Error!")

def clear_joke():
    joke_label.config(text="Press the button to see a joke!")
    status_label.config(text="Joke cleared")

root = tk.Tk()
root.title("Jokes Generator Python")

title_label = tk.Label(root, text="🐍 Jokes Generator Python 🐍", font=('Arial', 16))
title_label.pack()

instruction_label = tk.Label(root, text="Press the button to see a joke:", font=('Arial', 12))
instruction_label.pack()

joke_button = tk.Button(root, text="Random joke", width=20, height=2, command=get_joke)
joke_button.pack()

clear_button = tk.Button(root, text="Clear", width=20, height=2, command=clear_joke)
clear_button.pack()

# Etykieta dla wyświetlania żartu
joke_label = tk.Label(root, text="Press the button to see a joke!", 
                     width=60, height=8, wraplength=400, 
                     font=('Arial', 11), relief="sunken")
joke_label.pack()

status_label = tk.Label(root, text="Ready to generate jokes!", font=('Arial', 10))
status_label.pack()

root.mainloop()

