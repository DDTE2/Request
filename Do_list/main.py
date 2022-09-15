from tkinter import *
from tkinter import ttk

import sys


class Do:
    def __init__(self, project_path):
        self.project_path = project_path

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
    ## Запуск окна
    def run(self):

        self.window.mainloop()