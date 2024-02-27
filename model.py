from core import Specifications_Shoes, Types_Shoes, Colors_Shoes, List_type_shoes, Shoes
from pathlib import Path


class Model():
    def show_shoes(self):
        if Path("shoes.txt").exists():
            with open("shoes.txt", "r", encoding="utf-8") as file:
                return file.readlines()
        else:
            return None


    def add_shoes(self, list_shoes):
        with open("shoes.txt", "a", encoding="utf-8") as file:
            for line in list_shoes:
                file.writelines(line + " ")
            file.writelines("\n")

    def edit_shoes(self, num):
        with open("shoes.txt", "r", encoding="utf-8") as file:
            old_data = file.readlines()
            old_data[num[0]] = num[1]
