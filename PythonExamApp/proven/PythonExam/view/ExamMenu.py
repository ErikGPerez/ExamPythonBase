from proven.PythonExam.view.Option import Option
from proven.PythonExam.view.Menu import Menu

class ExamMenu(Menu):
    def __init__(self):
        super().__init__("Exam App Main Menu")
        self.addOption(Option("Exit", "exit"))