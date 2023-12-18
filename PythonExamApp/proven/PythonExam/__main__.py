from proven.PythonExam.model.ExamModel import ExamModel
from proven.PythonExam.controller.ExamController import ExamController

##Init main to run programm
class Main:
    def __init__(self):
        model = ExamModel()
        control = ExamController(model)

main = Main()