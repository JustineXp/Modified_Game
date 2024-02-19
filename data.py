from random import randint


class Data:

    def __init__(self):
        self.question_data = []

    def questions_number(self, operator):
        questions_number = int(
            input('How many Questions do you want to try  : '))
        self.updating_data(questions_number, operator)

    def updating_data(self, questions_number, operator):
        # print(operator)
        for i in range(questions_number):
            num1, num2, answer = self.random_generator(operator)
            self.question_data.append({
                'question_number': i+1,
                'number1': num1,
                'number2': num2,
                'answer': answer
            })
            i += 1

    @classmethod
    def random_generator(cls, operator):
        num1 = randint(1, 9)
        num2 = randint(1, 9)
        # print(operator)
        if (operator == '+'):
            answer = num1 + num2
        elif operator == '/':
            answer = num1 / num2
        elif operator == '-':
            answer = num1 - num2
        elif operator == '*':
            answer = num1 * num2
        return num1, num2, answer
