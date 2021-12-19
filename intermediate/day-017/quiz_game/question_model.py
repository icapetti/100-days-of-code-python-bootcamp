class Question():
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

new_question = Question("Rome is the capital of Italy?", "True")
print(new_question.question)