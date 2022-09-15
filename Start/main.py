from tkinter import *
from tkinter import ttk

import sys
from json import dumps, loads


class autorization:
    def __init__(self, project_path):
        self.project_path = project_path

        ## Настройка окна
        self.window = Tk()
        self.window.eval('tk::PlaceWindow . center')
        self.window.attributes("-topmost",True)

        self.window.iconbitmap(self.project_path + '/icons/lock.ico')

        self.window.title("Подключение к базе данных")
        self.window.geometry("350x150")
        self.window.resizable(width=False, height=False)

        ## Прекращение работы программы при закрытии окна
        self.window.protocol("WM_DELETE_WINDOW", lambda: sys.exit())
    def databases_input(self):
        with open(self.project_path + '/Data/database.data', 'r') as file:
            database_data = []
            self.databases = {}
            for i in file.read().split('\n'):
                databes = loads(i)
                x = databes['db_name']

                database_data.append(x)
                self.databases[x] = databes


        self.database = ttk.Combobox(self.window, state="readonly", values=database_data)

        self.database.grid(column=0, row=1)
        self.database.place(x=170, y=20)

        self.database.current(0)

        database_choise = Label(self.window, text='Выберите базу данных')
        database_choise.place(x=30, y=20)

    def connect_button(self):
        conn = Button(self.window,
                      text="Подключится к базе данных",
                      activebackground="pink",
                      activeforeground="blue",
                      command=self.connect)
        conn.grid(column=1, row=0)
        conn.place(x=100, y=50)

        _or = Label(self.window, text='или')
        _or.place(x=170, y=80)

    def new_connetc_button(self):
        conn = Button(self.window,
                      text="Подключится к другой базе данных",
                      activebackground="pink",
                      activeforeground="blue",
                      command=self.new_connect)
        conn.grid(column=1, row=0)
        conn.place(x=80, y=100)

    def new_connect(self):
        from SQL_data_input.main import SQL_data
        self.window.withdraw()
        self.window.quit()

        rez = SQL_data(self.project_path)
        rez.run()

    def connect(self):
        self.window.withdraw()
        self.window.quit()

        self.database = self.databases[self.database.get()]

    ## Запуск окна
    def run(self):
        self.databases_input()
        self.connect_button()
        self.new_connetc_button()

        self.window.mainloop()