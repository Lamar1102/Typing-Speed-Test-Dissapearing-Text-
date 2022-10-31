import random
import threading
from tkinter import *
from tkinter import ttk
import time
from threading import Timer,Thread
import ctypes


ctypes.windll.shcore.SetProcessDpiAwareness(1)

class Window:

    def __init__(self):
        ##Selecting random texts to type
        self.possibleTexts = [
            'For writers, a random sentence can help them get their creative juices flowing. Since the topic of the sentence is completely unknown, it forces the writer to be creative when the sentence appears. There are a number of different ways a writer can use the random sentence for creativity. The most common way to use the sentence is to begin a story. Another option is to include it somewhere in the story. A much more difficult challenge is to use it to end a story. In any of these cases, it forces the writer to think creatively since they have no idea what sentence will appear from the tool.',
            'The goal of Python Code is to provide Python tutorials, recipes, problem fixes and articles to beginner and intermediate Python programmers, as well as sharing knowledge to the world. Python Code aims for making everyone in the world be able to learn how to code for free. Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.',
            'As always, we start with the imports. Because we make the UI with tkinter, we need to import it. We also import the font module from tkinter to change the fonts on our elements later. We continue by getting the partial function from functools, it is a genius function that excepts another function as a first argument and some args and kwargs and it will return a reference to this function with those arguments. This is especially useful when we want to insert one of our functions to a command argument of a button or a key binding.'
        ]
        self.text = random.choice(self.possibleTexts)
        self.length_of_text = len(self.text)

        #Correct words
        self.correct_words = 0

        #User Inputs
        self.user_input = None

        #Window setup
        self.window = Tk()
        self.window.title("Speed Typing Test")
        self.window.geometry("500x500")
        self.frame = ttk.Frame(self.window, padding=20)
        self.frame.grid()
        # Row and Column configuration for centering
        self.frame.grid(row=0, column=0, sticky="NESW")
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)


        self.characters_correct = 0
        self.left_label_text = ""
        self.right_label_text = self.text[self.characters_correct:self.characters_correct + 10]

        self.time = 60
        #Running Functions
        self.begin_button()
        self.keypress()
        # Opens window when run
        self.window.mainloop()

    def begin_button(self):
        self.begin_button = ttk.Button(self.frame,text="Start",command=self.labels)
        self.begin_button.grid(row=0,column=0)
    def timer_thread(self):
        timer_on = True
        while timer_on:
            time.sleep(1)
            self.time -=1
            self.timer_label.config(text=self.time)
            if self.time == 0:
                self.timer_label.destroy()
                self.user_input_label.destroy()
                self.left_text_label.destroy()
                self.right_text_label.destroy()
                timer_on=False
                self.finish()

    def labels(self):
        time.sleep(0.25)
        thread= Thread(target=self.timer_thread)
        thread.start()
        self.begin_button.destroy()
        self.left_text_label = ttk.Label(self.frame, text=self.left_label_text, foreground="Black",font=28)
        self.right_text_label = ttk.Label(self.frame, text=self.right_label_text, foreground="Grey",font=28)
        self.user_input_label = ttk.Label(self.frame, text=self.user_input, foreground="Black",font=28)
        self.timer_label = ttk.Label(self.frame,text=self.time)

        self.left_text_label.place(relx=.25,rely=.5)
        self.right_text_label.place(relx=.60,rely=.5)
        self.user_input_label.place(relx=.5,rely=.5)
        self.timer_label.place(relx=0.5,rely=.25)

    def check_key(self,char):
        self.user_input_label.config(text=self.user_input)
        if char == self.right_label_text[0]:
            self.left_label_text += char
            self.left_label_text = self.left_label_text[-10:]
            self.characters_correct += 1
            self.right_label_text = self.text[self.characters_correct:self.characters_correct+10]

            if char == " ":
                self.correct_words +=1

            self.left_text_label.config(text=self.left_label_text)
            self.right_text_label.config(text=self.right_label_text)
    def finish(self):
        correct_words_label = ttk.Label(self.frame,text=f"You typed {self.correct_words} words per minute!")
        correct_words_label.grid(row=0,column=0)

        restart_button = ttk.Button(self.frame, text="Restart",command=self.restart)
        restart_button.grid(row=1,column=0)
        print(threading.currentThread())
    def restart(self):
        self.window.destroy()
        Window()
##Detects the keypres
    def keypress(self):
        def key_pressed(event):
            self.user_input = event.char
            #Runs function check_key with character user input to see if
            self.check_key(self.user_input)
        self.window.bind("<Key>", key_pressed)
Window()
