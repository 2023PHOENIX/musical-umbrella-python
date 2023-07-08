class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = -1
        self.question_bank = question_bank
        self.score = 0;

    def is_available(self):
        return self.question_number < len(self.question_bank) - 1

    def next_question(self):
        self.question_number += 1
        return self.question_bank[self.question_number]

    def score_cal(self):
        print(f"your current score is {self.score} / {self.question_number + 1}")

    def validate_answer(self, response):
        if response.capitalize() == self.question_bank[self.question_number].answer:
            self.score += 1
            print("you are correct")
            return True

        self.score_cal()
        print("sorry your answer is incorrect")

        return False

