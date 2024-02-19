from data import Data
from question_model import Question
from quiz_brain import QuizBrain


data = Data()
operator = QuizBrain.operator_switcher(QuizBrain.operator_request())
data.questions_number(operator)
question_data = data.question_data

print(question_data)

question_bank = [Question(question['question_number'], question['number1'], question['number2'], question['answer'])
                 for question in question_data]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print('You have completed the quiz.')
print(f'Final score was : {quiz.score}/{len(question_bank)}')
