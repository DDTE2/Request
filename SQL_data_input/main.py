from tkinter import *
from tkinter import ttk

import sys
from json import dumps

from SQL_data_input.MySQL import create_connection

class SQL_data:
    def __init__(self, project_path):
        self.project_path = project_path
        self.massenge_flag = False

        ## Настройка окна
        self.window = Tk()
        self.window.eval('tk::PlaceWindow . center')
        self.window.attributes("-topmost",True)

        self.window.iconbitmap(self.project_path + '/icons/SQL.ico')

        self.window.title("Получение доступа к базе данных")
        self.window.geometry("380x320")
        self.window.resizable(width=False, height=False)

        ## Прекращение работы программы при закрытии окна
        self.window.protocol("WM_DELETE_WINDOW", lambda: sys.exit())

    ## Тип базы данных
    def SQL_type(self):
        self.db_type = ttk.Combobox(self.window, state="readonly", values=["MySQL",
                                                                 "SQLite",
                                                                 "PostgreSQL",
                                                                 ])

        self.db_type = ttk.Combobox(self.window, state="disabled", values=["MySQL",
                                                                           "SQLite",
                                                                           "PostgreSQL",
                                                                           ])

        self.db_type.grid(column=0, row=1)
        self.db_type.place(x=170, y=20)

        self.db_type.current(0)

        type_text = Label(self.window, text='Тип базы даннх')
        type_text.place(x=30, y=20)

    ## Информация о хосте
    def host_choise(self):
        host_text = Label(self.window, text='Хост')
        host_text.place(x=30, y=50)

        self.host = Entry(self.window, width=23)
        self.host.grid(column=1, row=0)
        self.host.place(x=170, y=50)

    def port_choise(self):
        port_text = Label(self.window, text='Порт')
        port_text.place(x=30, y=80)

        self.port = Entry(self.window, width=23)
        self.port.insert(END, 3306)
        self.port.grid(column=1, row=0)
        self.port.place(x=170, y=80)

    ## Информация о пользователе
    def user_name(self):
        user_text = Label(self.window, text='Имя пользователя')
        user_text.place(x=30, y=110)

        self.user = Entry(self.window, width=23)
        self.user.grid(column=1, row=0)
        self.user.place(x=170, y=110)

    def user_password(self):
        password_text = Label(self.window, text='Пароль')
        password_text.place(x=30, y=140)

        self.password = Entry(self.window, width=23, show='*')
        self.password.grid(column=1, row=0)
        self.password.place(x=170, y=140)

    ## Показ пароля
    def showing_password_button(self):
        self.showing_button = ttk.Checkbutton(self.window, text='Показывать пароль', command=self.show_password)
        self.showing_button.place(x=170, y=170)

    def show_password(self):
        if 'selected' in self.showing_button.state():
            self.password.config(show='')
        else:
            self.password.config(show='*')

    ## Имя базы данных
    def database_name(self):
        db_text = Label(self.window, text='Название базы данных')
        db_text.place(x=30, y=200)

        self.db = Entry(self.window, width=23)
        self.db.grid(column=1, row=0)
        self.db.place(x=170, y=200)

    ## Сохранение и проверка данных
    def save_data_button(self):
        save = Button(self.window,
                      text="Сохранить данные",
                      activebackground="pink",
                      activeforeground="blue",
                      command=self.save_data)
        save.grid(column=1, row=0)
        save.place(x=140, y=230)

    def save_data(self):
        match self.db_type.get():
            case 'MySQL':
                self.data = {'db_type': self.db_type.get(),
                             'host': self.host.get(),
                             'port': int(self.port.get()),
                             'user_name': self.user.get(),
                             'password': self.password.get(),
                             'db_name': self.db.get()}

                if '' in self.data.values():
                    self.massenge(error='Все поля должны быть заполнены!')
                else:
                    rez = create_connection(self.host.get(), self.port.get(), self.user.get(), self.password.get(), self.db.get())
                    if rez == 'Error':
                        self.massenge(error='При подключении к базе данных произошла ошибка!')
                    else:
                        with open(self.project_path + '/Data/database.data', 'r') as file:
                            file_data = file.read().split('\n')

                        data = dumps(self.data)
                        if file_data != ['']:
                            if not(data in file_data):
                                with open(self.project_path + '/Data/database.data', 'a') as file:
                                    file.write('\n' + data)
                        else:
                            with open(self.project_path + '/Data/database.data', 'w') as file:
                                file.write(data)
                        self.massenge(text='Данные успешно сохранены.')



            case 'SQLite':
                self.data = {'db_type': self.db_type.get(),
                             'host': self.host.get(),
                             'port': self.port.get(),
                             'user_name': self.user.get(),
                             'password': self.password.get(),
                             'db_name': self.db.get()}

    ## Отчистка данных
    def clean_data_button(self):
        save = Button(self.window,
                      text="Отчистить данные",
                      activebackground="pink",
                      activeforeground="blue",
                      command=self.clean_data)
        save.grid(column=1, row=0)
        save.place(x=140, y=260)

    def clean_data(self):
        self.db_type.current(0)
        self.host.delete('0', END)
        self.port.delete('0', END)
        self.port.insert(END, 3306)
        self.user.delete('0', END)
        self.password.delete('0', END)
        self.db.delete('0', END)

    ## Сообщения для пользователя
    def massenge(self, text=None, error=None):
        if self.massenge_flag:
            if text:
                self.massenge_text.config(text=text, fg='blue')
            elif error:
                self.massenge_text = Label(text=error, fg='red')
                self.massenge_text.place(x=30, y=290)
            else:
                self.massenge_text = Label(self.window)
                self.massenge_text.place(x=30, y=290)
        else:
            self.massenge_text = Label(self.window, text='', fg='blue')
            self.massenge_text.place(x=30, y=290)

            self.massenge_flag = True

    ## Запуск окна
    def run(self):
        self.SQL_type()
        self.host_choise()
        self.port_choise()
        self.user_name()
        self.user_password()
        self.showing_password_button()
        self.database_name()
        self.save_data_button()
        self.clean_data_button()
        self.massenge()

        self.window.mainloop()