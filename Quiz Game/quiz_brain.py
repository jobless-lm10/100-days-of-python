class QuizBrain:
    def __init__(self, question_book):
        self.question_number = 0
        self.questions_list = question_book
        self.score = 0

    def next_question(self):
        user_answer = input(f"Q.{self.question_number+1}: {self.questions_list[self.question_number].text} (True/False)?: ")
        self.check_answer(user_answer, self.questions_list[self.question_number].answer)
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Sorry, you got it wrong.")
        print(f"Your current score is: {self.score}/{self.question_number+1}")
