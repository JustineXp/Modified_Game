class QuizBrain:
    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0
        self.choice = 0
        self.operator
        self.repeat = True

    @classmethod
    def operator_request(cls):
        operators_list = ['Multiplication',
                          'Addition', 'Subtraction', 'Division']
        operator_string = '\n1: Multiplication\n2: Addition\n3: Subtraction\n4: Division\n\n'
        while True:
            try:
                cls.choice = int(input(operator_string.upper()))
                if cls.choice <= 0 or cls.choice > 4:
                    print('Use numbers 1-4 to make a selection.')
                else:
                    print(f'{operators_list[cls.choice-1].upper()} SELECTED')
                    cls.operator_switcher(cls.choice)
                    return cls.choice
            except ValueError:
                print(
                    'You did not enter a number,\nUse numbers 1-4 to make a selection.')

    @classmethod
    def operator_switcher(cls, operator_choice):
        choices_list = []
        operators = {
            'Multiplication': '*',
            'Addition': '+',
            'Subtraction': '-',
            'Division': '/'
        }

        for _ in operators.values():
            choices_list.append(_)
        operator = choices_list[cls.choice-1]
        cls.operator = operator
        return operator

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def question_user(self, question):
        try:
            while True:
                user_response = int(input(
                    f'Question {question.question_number} : {question.num1} {self.operator} {question.num2} = '))
                if self.repeat:
                    if user_response == question.answer:
                        self.check_answer(user_response, question.answer)
                        break
                    else:
                        while self.repeat:
                            if self.repeat:
                                print(
                                    f'{user_response} is not correct.')
                            resp = input(
                                'YOU HAVE ONE CHANCE TO REPEAT THE QUESTION.\nDO YOU WANT TO TRY AGAIN ? (YES/NO) ')
                            if resp.lower() == 'yes':
                                self.repeat = False
                            elif resp.lower() == 'no':
                                self.check_answer(
                                    user_response, question.answer)
                                print()
                                print()
                                return
                            else:
                                print()
                                print()
                                print('Please use Yes or No ans your response')
                else:
                    self.check_answer(user_response, question.answer)
                    # print('testing . . .')
                    self.repeat = True
                    break
        except ValueError:
            print('You didn\'t enter a number.')

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        self.question_user(question)

    def check_answer(self, user_response, correct_answer):
        if user_response == correct_answer:
            self.score += 1
            print('You Got it Right.')
        else:
            if self.repeat:
                print('You skipped the question.')
            else:
                print('You didn\'t get it right')
        print(f'{correct_answer} was the right answer')
        print(
            f'YOUR CURRENT SCORE IS : {self.score}/{self.question_number}\n\n')
