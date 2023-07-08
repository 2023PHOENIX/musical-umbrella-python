from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for d in question_data:
    question_bank.append(Question(d["text"], d["answer"]))

qb = QuizBrain(question_bank)

while qb.is_available():
    q = qb.next_question()
    print(f"Q {qb.question_number}. {q.text} ?")
    response = input()

    ans = qb.validate_answer(response)



print("you have completed the quiz 👌");
qb.score_cal();