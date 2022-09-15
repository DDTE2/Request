from tkinter import *
from tkinter import ttk

import sys
from json import dumps, loads

from SQL_data_input.MySQL import create_connection

class autorization:
    def __init__(self, project_path):
        self.project_path = project_path

        ## Настройка окна
        self.window = Tk()
        self.window.eval('tk::PlaceWindow . center')
        self.window.attributes("-topmost",True)

        self.window.iconbitmap(self.project_path + '/icons/lock.ico')

        self.window.title("Подключение к базе данных")
        self.window.geometry("380x320")
        self.window.resizable(width=False, height=False)

        ## Прекращение работы программы при закрытии окна
        self.window.protocol("WM_DELETE_WINDOW", lambda: sys.exit())
    def databases_input(self):
        with open(self.project_path + '/Data/database.data', 'r') as file:
            databases_import = lambda x: loads(x)['db_name']
            *database_data, = map(databases_import, file.read().split('\n'))
            print(database_data)

        self.db_type = ttk.Combobox(self.window, state="readonly", values=database_data)

        self.db_type.grid(column=0, row=1)
        self.db_type.place(x=170, y=20)

        self.db_type.current(0)

    ## Запуск окна
    def run(self):
        self.databases_input()
        self.window.mainloop()