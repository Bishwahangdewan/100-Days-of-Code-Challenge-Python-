from data import question_data
from question_model import Questions


class QuizzBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        text = self.question_list[self.question_number].question
        correct_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        your_answer = input(f"Q {self.question_number}  {text} ? (True or False)")
        self.check_answer(your_answer, correct_answer)

    def check_answer(self, your_answer, correct_answer):
        if your_answer.lower() == correct_answer.lower():
            print("You are Correct !")
            self.score += 1
        else:
            print("you are wrong !")
        print(f"The correct answer is {correct_answer} ")
        print(f"Your score is {self.score}/{self.question_number}")
