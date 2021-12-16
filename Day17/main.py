from data import question_data
from question_model import Questions
from quiz_brain import QuizzBrain

question_bank = []

for i in question_data:
    question_bank.append(Questions(i["text"], i["answer"]))

quiz = QuizzBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz?")
print(f"Your Final Score is {quiz.score}/{len(question_bank)}")