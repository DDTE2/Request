from tkinter import *
from tkinter import ttk

import sys


class Do:
    def __init__(self, project_path, database):
        self.project_path = project_path
        self.database = database

        ## Настройка окна
        self.window = Tk()
        self.window.eval('tk::PlaceWindow . center')
        self.window.attributes("-topmost",True)

        self.window.iconbitmap(self.project_path + '/icons/SQL.ico')

        self.window.title("Выбор команды")
        self.window.geometry("380x320")
        self.window.resizable(width=False, height=False)

        ## Прекращение работы программы при закрытии окна
        self.window.protocol("WM_DELETE_WINDOW", lambda: sys.exit())
    def make_button(self):
        button = Button(self.window,
                      text="Создать таблицы",
                      activebackground="pink",
                      activeforeground="blue",
                      command=self.make)
        button.place(x=30, y=20)
    def make(self):
        from Do_list.creat_database.creat import table_gen
        table_gen(path=self.project_path, database_data=self.database)

    def generate_button(self):
        button = Button(self.window,
                        text="Заполнить таблицы случайными значениями",
                        activebackground="pink",
                        activeforeground="blue",
                        command=self.generate)
        button.place(x=30, y=50)
    def generate(self):
        from Do_list.random_data.request import table_gen
        table_gen(path=self.project_path, database_data=self.database)


    ## Запуск окна
    def run(self):
        self.make_button()
        self.generate_button()

        self.window.mainloop()