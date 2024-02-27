from model import Model
from view import View

class Presenter:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def main(self):
        quest = ["1", "2", "3", "4"]
        answer_questions = self.view.main()
        while answer_questions not in quest:
            answer_questions = self.view.main()
        if answer_questions == "1":
            show = self.model.show_shoes()
            self.view.show(show)
        elif answer_questions == "2":
            add_show_view = self.view.add_shoes()
            add_show_model = self.model.add_shoes(add_show_view)
            self.view.show(add_show_model)
        elif answer_questions == "3":
            edit_show = self.view.edit_shoes()
            self.model.edit_shoes(edit_show)
        else:
            pass





if __name__ == '__main__':
    presenter = Presenter()
    presenter.main()