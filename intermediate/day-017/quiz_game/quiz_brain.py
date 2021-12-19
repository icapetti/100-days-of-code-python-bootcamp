class QuizBrain():

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_question(self):
        """
        Return True if there are still questions left in the question list.
        Return False if there are no questions left.
        """

        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Retrieve the item at the current question_number from the question list.
        Use the input() function to show the user the question text and 
        ask the user for the answer.
        """

        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.question} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, answer):
        """
        Check if the user's answer is correct.
        If the user's answer is correct, increment the score.
        """

        if user_answer.lower() == answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("Wrong!")
        print(f"The correct answer was {answer}")
        print(f"Your score is {self.score}")