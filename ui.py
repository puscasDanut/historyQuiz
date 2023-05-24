from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title = "General Knowledge Quiz"
        self.window.config(bg=THEME_COLOR)
        self.window.minsize(width=350, height=500)

        self.score_label = Label(text=f"Score: 0")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas()

        self.window.mainloop()
