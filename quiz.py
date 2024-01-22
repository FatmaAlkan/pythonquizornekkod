class Questions():
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def CheckAnswer(self, answer):
        return self.answer == answer


class Quiz():
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuastion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):  #amacım questionı göstermek
        question = quiz.getQuastion()
        print(f'soru {self.questionIndex+1} : {question.text}')

        for q in question.choices:
            print('-'+q)

        answer = input('cevabiniz: ')
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuastion()

        if question.CheckAnswer(answer):    #doğru yanıt durumunda score 1 artar
            self.score += 1 
        self.questionIndex +=1

    
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print ('score: ', self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1 

        if questionNumber > totalQuestion:
            print('Quiz Biti')
        else:
            print(f'Question {questionNumber} of {totalQuestion} '.center(50,'*'))

q1 = Questions('En iyi progamlama dili hangisidir', ['C','PYTHON','JAVA','PHP'], 'PYTHON')
q2 = Questions('En popüler progamlama dili hangisidir', ['C','PYTHON','JAVA','PHP'], 'PYTHON')
q3 = Questions('En cok tercih edilen progamlama dili hangisidir', ['C','PYTHON','JAVA','PHP'], 'JAVA')
questions = [q1, q2, q3]

quiz = Quiz (questions)
quiz.loadQuestion()