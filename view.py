from core import List_type_shoes

class View:
    def main(self) -> str:
        comm: str = input("""
            1. Просмотр базы обуви
            2. Добавление обуви в базу
            3. Редактирование позиции в базе
            4. Удаление позиции из базы
        """)
        return comm

    def show(self, zapros):
        if zapros is None:
            print("Обуви на складе нет!")
        else:
            print(zapros)

    def add_shoes(self):
        add_shoes_list = []
        for i in List_type_shoes:
            zap = input(f"Введите {i.value} - ")
            while zap == "":
                zap = input(f"Вы ввели пустую строку. Введите {i.value} - ")
            add_shoes_list += [zap]
        return add_shoes_list


    def edit_shoes(self):
        edit_sh = input("Введите номер строки для редактирования - ")
        edit_sss = self.add_shoes()
        return edit_sh, edit_sss


    def test(self, num, text):
        if num == 0:
            pass
        if num == 0:
            pass
        if num == 0:
            pass
        if num == 0:
            pass
        if num == 0:
            pass
        if num == 0:
            pass








