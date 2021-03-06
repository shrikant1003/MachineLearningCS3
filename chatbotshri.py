# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 13:31:14 2020

@author: ACER
"""
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#Creating an instance of ChatBot
chatbot = ChatBot("BotKant")

#Converstion for ChatBot
conversation = [
    "Good morning",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "Ask me something.",
    "What is your name",
    "My name is BotKant."
]

#Training ChatBot
trainer = ListTrainer(chatbot)
trainer.train(conversation)

################GUI################
#Importing basic libraries required
from tkinter import *

#funcion to respond to user queries
def ask():
    query=text.get()
    answer=chatbot.get_response(query)
    msg.insert(END, "you :" +query)
    msg.insert(END, "bot :" + str(answer))
    text.delete(0,END)

#Creating a window
window = Tk()
window.title("BotKant")
window.geometry("500x650")

#image for label
img = PhotoImage(file='image.png')

#adding a label
lbl = Label(window, image=img)
lbl.pack()

frame = Frame(window)

#Creating a ScrollBar
sc = Scrollbar(frame)
msg = Listbox(frame, width=80, height=20)
sc.pack(side=RIGHT, fill=Y)
msg.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()
#Creating a text entry field
text = Entry(window, font=("Verdana", 16))
text.pack(pady=10)

#Creating a Button
btn = Button(window, text="Send", command=ask)
btn.pack()

#To run forever
window.mainloop()