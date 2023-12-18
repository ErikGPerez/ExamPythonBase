from proven.PythonExam.view.ExamMenu import ExamMenu
from proven.PythonExam.model.ExamModel import ExamModel
from proven.PythonExam.controller.ExamController import *
class ExamView:
    def __init__(self, control, model):
        self.control = control
        self.model = model
        self.menu = ExamMenu()
    def display(self):
        while True:
            self.menu.show()
            action = self.menu.getSelectedOptionActionCommand()
            self.processAction(action)
    def processAction(self, action):
        if action != None:
            if action:
                self.control.processRequest(action)
    def showInputDialog(self, message):
        print(message)
        return input()
    
    def showMessage(self, message):
        print(message)