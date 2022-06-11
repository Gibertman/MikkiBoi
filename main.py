from tkinter import * # используется для создания gui
from PIL import ImageTk
import speech_recognition as sr # библиотека распознование голоса
import webbrowser
from datetime import datetime
from tkinter.ttk import Notebook
import pyautogui as pg
import pyttsx3

import os
class mikki:
    def __init__(self):
        self.window = Tk()
        self.window['bg'] = 'white'
        self.window.iconbitmap('logo.ico')
        self.window.resizable(False, False)
        self.window.title("Voice assistent Mikki")
        self.window.geometry('400x600'.format(300, 0))
        # выше реализованы параметры окошка, в котором пользователь будет совершать действия
        self.imageq = ImageTk.PhotoImage(file="lg1.png")
        self.nowimageq = self.imageq
        self.imageq2 = ImageTk.PhotoImage(file="lg2.png")
        self.imageq3 = ImageTk.PhotoImage(file="lg3.png")
        self.imageq4 = ImageTk.PhotoImage(file="lg4.png")
        self.tapped = ImageTk.PhotoImage(file="microtapped.png")
        self.pushed_flag = 0
        self.image = self.imageq
        self.tabs_control = Notebook(self.window)
        self.tab_1 = Frame(self.tabs_control, bg='white')
        self.tabs_control.add(self.tab_1, text="Окно асситента")
        self.tab_2 = Frame(self.tabs_control, bg='white')
        self.tabs_control.add(self.tab_2, text="История поиска")
        self.tab_3 = Frame(self.tabs_control, bg='white')
        self.tabs_control.add(self.tab_3, text="Инструкция")
        self.tab_4 = Frame(self.tabs_control, bg='white')
        self.tabs_control.add(self.tab_4, text="Оформление")

    def draw_widgets(self):
        self.tabs_control.pack(fill=BOTH, expand=1)
    def clicked(self):  # функция отвечает за смену состояния кнопки, а именно приводит в действие распознование голоса и последующие команды
        self.textspeech.delete(1.0, "end")
        self.textmikki.delete(1.0, "end")
        if self.pushed_flag == 0:
            self.pushed_flag = 1
            self.say_message('Говорите..')  # проигрывание голосового сообщения от ассистента
            self.microtapped()

            self.pushed_flag = 0
    def story(self):
        self.textstory = Text(self.tab_2, width=46, height=33, borderwidth=1)
        self.textstory.place(x=10, y=20)
    def microtapped(self):  # функция отвечает за выполнение команды введенной пользователем
        command = self.listen_command()  # прослушивание
        self.do_this_command(command)  # выполнение команды
        self.textspeech.insert("insert", 'Вы:' + '\n' + command + '\n')  # текст речи пользователя
        self.textstory.insert("insert", 'Вы:' + '\n' + command + '\n') # смена изображения кнопки почему-то работает некорректно

    def listen_command(self):  # функция прослушивания сообщения поьзователя
        r = sr.Recognizer()
        with sr.Microphone() as source:  # источник аудио
            print('Скажите вашу команду!')
            audio = r.listen(source)
        # recognize speech using Google Speech Recognition
        try:
            our_speech = r.recognize_google(audio, language="ru")
            print('Вы сказали: ' + our_speech)
            return our_speech
        except sr.UnknownValueError:  # ошибка значения
            return 'ошибка'
        except sr.RequestError:  # ошибка запроса
            return 'ошибка'

    def do_this_command(self, message):  # выполнение команды
        message = message.lower()  # перевод сообщения к нижнему регистру для распознования
        if 'привет' in message:  # различные варианты ввода
            ans = 'Привет, товарищ, сейчас я тестирую постепенный вывод строки в окошко, поэтому не ругайся)'
            s = 'Mikki:' + '\n' + ans + '\n'
            self.say_message(ans)
            self.textmikki.insert("insert", s)
            self.textstory.insert("insert", 'Mikki:' + '\n' + ans + '\n')
        elif 'пока' in message:  # это тестовый вариант ответов, поэтому такой примитив
            ans = 'Пока!'
            self.textmikki.insert("insert", 'Mikki:' + '\n' + ans + '\n')
            self.textstory.insert("insert", 'Mikki:' + '\n' + ans + '\n')
            self.say_message(ans)
            sys.exit()
        elif 'открой youtube' in message:
            self.say_message("Открываю")
            self.textmikki.insert("insert", 'Mikki:' + '\n' + "Открываю" + '\n')
            self.textstory.insert("insert", 'Mikki:' + '\n' + "Открываю" + '\n')
            url = 'https://www.youtube.com/'
            webbrowser.open(url)
        elif 'открой сайт с погодой' in message:
            self.say_message("Открываю")
            self.textmikki.insert("insert", 'Mikki:' + '\n' + "Открываю" + '\n')
            self.textstory.insert("insert", 'Mikki:' + '\n' + "Открываю" + '\n')
            url = 'https://rp5.ru'
            webbrowser.open(url)

        elif 'своё имя' in message:
            self.say_message("Меня зовут Микки")
            self.textmikki.insert("insert", 'Mikki:' + '\n' + "Меня зовут Микки" + '\n')
            self.textstory.insert("insert", 'Mikki:' + '\n' + "Меня зовут Микки" + '\n')

        elif 'меня зовут' in message:
            self.say_message("Классное имя")
            self.textmikki.insert("insert", 'Mikki:' + '\n' + "Классное имя" + '\n')
            self.textstory.insert("insert", 'Mikki:' + '\n' + "Классное имя" + '\n')

        elif 'спасибо' in message:
            self.say_message("Всегда пожалуйста")
            self.textmikki.insert("insert", 'Mikki:' + '\n' + "Всегда пожалуйста" + '\n')
            self.textstory.insert("insert", 'Mikki:' + '\n' + "Всегда пожалуйста" + '\n')
        elif 'открой блокнот' in message:
            os.system("notepad.exe")
        elif 'сколько времени' in message:
            now = datetime.now()
            text = "Сейчас " + str(now.hour) + ":" + str(now.minute)
            self.say_message(text)
            self.textmikki.insert("insert", 'Mikki:' + '\n' + text + '\n')
            self.textstory.insert("insert", 'Mikki:' + '\n' + text + '\n')
        elif 'запиши в блокнот' in message:
            self.say_message("Что мне записать?")
            self.textmikki.insert("insert", 'Mikki:' + '\n' + "Что мне записать?" + '\n')
            self.textmikki.insert("insert", 'Mikki:' + '\n' + "Что мне записать?" + '\n')
            note = self.listen_command()
            file = open('zametka.txt', 'w')
            file.write(note)
        elif 'скриншот' in message:
            pg.screenshot("yourPic.png")
            self.textmikki.insert("insert", 'Mikki:' + '\n' + "Сделал скриншот" + '\n')
            self.textstory.insert("insert", 'Mikki:' + '\n' + "Сделал скриншот" + '\n')
        elif 'найди в гугле' in message:
            message = message.replace('найди в гугле', ' ')
            url = "https://google.com/search?q=" + message
            webbrowser.open(url)
        else:
            self.say_message(message)

    def say_message(self, message):  # функция, обеспечивающая диалог ассистента с пользователем
        tts = pyttsx3.init()
        tts.setProperty('voice', 'ru')
        tts.say(message)
        tts.runAndWait()
        print('Голосовой ассистент: ' + message)  # вывод сообщения в консоль

    def Button(self):

        self.btn = Button(self.tab_1, image=self.nowimageq, height=100, width=100,
                     activebackground='white', command=self.clicked, borderwidth=0, bg='white')
        self.btn.place(x=150, y=450)
    def micro1(self):
        self.btn.configure(image=self.imageq)
        self.nowimageq = self.imageq
    def micro2(self):
        self.btn.configure(image=self.imageq2)
        self.nowimageq = self.imageq2
    def micro3(self):
        self.btn.configure(image=self.imageq3)
        self.nowimageq = self.imageq3
    def micro4(self):
        self.btn.configure(image=self.imageq4)
        self.nowimageq = self.imageq4
    def design(self):
        instruction = 'Кликните по макету кнопки, чтобы\nизменить кнопку в окне ассистента'
        lbl = Label(self.tab_4, text=instruction, bg='white', font='Arial 13')
        lbl.place(x=50, y=50)
        self.des_btn1 = Button(self.tab_4, image=self.imageq, height=100, width=100,
                     activebackground='white', command=self.micro1, borderwidth=0, bg='white')
        self.des_btn1.place(x=70, y=150)
        self.des_btn2 = Button(self.tab_4, image=self.imageq2, height=100, width=100,
                               activebackground='white', command=self.micro2, borderwidth=0, bg='white')
        self.des_btn2.place(x=220, y=150)
        self.des_btn3 = Button(self.tab_4, image=self.imageq3, height=100, width=100,
                               activebackground='white', command=self.micro3, borderwidth=0, bg='white')
        self.des_btn3.place(x=70, y=300)
        self.des_btn4 = Button(self.tab_4, image=self.imageq4, height=100, width=100,
                               activebackground='white', command=self.micro4, borderwidth=0, bg='white')
        self.des_btn4.place(x=220, y=300)

    def textwindows(self, tab):
        self.textspeech = Text(tab, width=45, height=5, borderwidth=1)
        self.textspeech.place(x=10, y=100)
        self.textmikki = Text(self.tab_1, width=45, height=5, borderwidth=1)
        self.textmikki.place(x=10, y=200)
        # установка всех конфигураций кнопок, диалоговых окон, всех размеров, цветов,
        # картинок и логотипов и подключение реализованного управления голосом
    def run(self):
        self.textwindows(self.tab_1)
        self.Button()
        self.story()
        self.design()
        self.draw_widgets()
        self.window.mainloop()  # запуск окна


window = mikki()
window.run()
