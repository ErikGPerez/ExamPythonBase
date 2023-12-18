from proven.PythonExam.view.ExamView import ExamView
from proven.PythonExam.model.ExamModel import ExamModel
class ExamController:
    def __init__(self, model: ExamModel()):
        self.model = model
        self.view = ExamView(self, self.model)
        self.view.display()

    def processRequest(self, action):
        if (action == None):
            action = "wrong_action"
        match action:
            case "exit":
                self.exitApplication()
            case _:
                self.view.showMessage("Wrong Option")
    #exit
    def exitApplication(self):
        quit()