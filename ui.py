from tkinter import *
import os
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

main_dir = os.path.dirname(__file__)


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("General Knowledge Quizz")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.window.minsize(width=350, height=500)

        right_button_img = PhotoImage(file=main_dir + "./images/true.png")
        wrong_button_img = PhotoImage(file=main_dir + "./images/false.png")

        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 12))
        self.score_label.grid(column=1, row=0, padx=(50, 0), pady=(0, 20))

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text=f"Lorem Ipsum",
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(column=0, columnspan=2, row=1)

        self.yes_button = Button(image=right_button_img, highlightthickness=0, command=self.chose_true)
        self.yes_button.grid(column=0, row=2, pady=40)

        self.no_button = Button(image=wrong_button_img, highlightthickness=0, command=self.chose_false)
        self.no_button.grid(column=1, row=2, pady=40)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"The Quiz has finished\nFinal Score: {self.quiz.score}")
            self.yes_button.config(state="disabled")
            self.no_button.config(state="disabled")

    def chose_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def chose_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.window.after(1000, func=self.get_next_question)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, func=self.get_next_question)
