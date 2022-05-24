from tkinter import * # используется для создания gui
from PIL import ImageTk # для грамотного импорта изображений
import sys # для системных команд
from gtts import gTTS # перевод речи в голос
import random # рандом есть рандом
import time # импорт времени
import playsound # проигрывание звукозаписи
import speech_recognition as sr # библиотека распознование голоса
import webbrowser
import os


def clicked(): # функция отвечает за смену состояния кнопки, а именно приводит в действие распознование голоса и последующие команды
    global pushed_flag
    global textspeech
    global tapped, imageq
    x = False
    textspeech.delete(1.0, "end")
    textmikki.delete(1.0, "end")
    if pushed_flag == 0:
        btn.place(x=15, y=525)
        pushed_flag = 1
        btn.configure(height=60, width=60, image=tapped)
        say_message('Говорите..') # проигрывание голосового сообщения от ассистента
        x = True
    if x:
        microtapped()
        pushed_flag = 0


def microtapped(): # функция отвечает за выполнение команды введенной пользователем
    global textspeech, btn
    command = listen_command() # прослушивание
    do_this_command(command) # выполнение команды
    textspeech.insert("insert", 'Вы:' + '\n' + command + '\n') # текст речи пользователя
    btn.place(x=150, y=485) # изменение положения кнопки
    btn.configure(height=100, width=100, image=imageq) # смена изображения кнопки почему-то работает некорректно


def listen_command(): # функция прослушивания сообщения поьзователя
    r = sr.Recognizer()
    with sr.Microphone() as source: # источник аудио
        print('Скажите вашу команду!')
        audio = r.listen(source)
    # recognize speech using Google Speech Recognition
    try:
        our_speech = r.recognize_google(audio, language="ru")
        print('Вы сказали: ' + our_speech)
        return our_speech
    except sr.UnknownValueError: # ошибка значения
        return 'ошибка'
    except sr.RequestError: # ошибка запроса
        return 'ошибка'


def do_this_command(message): # выполнение команды
    message = message.lower() # перевод сообщения к нижнему регистру для распознования
    if 'привет' in message: # различные варианты ввода
        ans = 'Привет, товарищ'
        textmikki.insert("insert", 'Mikki:' + '\n' + ans + '\n')
        say_message(ans)
    elif 'пока' in message: # это тестовый вариант ответов, поэтому такой примитив
        ans = 'Пока!'
        textmikki.insert("insert", 'Mikki:' + '\n' + ans + '\n')
        say_message(ans)
        sys.exit()
    elif 'спой' in message:
        say_message('нет')
    elif 'время' in message:
        time = '12:58'
        textmikki.insert("insert", 'Mikki:' + '\n' + time + '\n')
        say_message(time)
    elif 'открой youtube' in message:
        say_message("Открываю")
        textmikki.insert("insert", 'Mikki:' + '\n' + "Открываю" + '\n')
        url = 'https://www.youtube.com/'
        webbrowser.open(url)
    else:
        say_message(message)


def say_message(message): # функция, обеспечивающая диалог ассистента с пользователем
    voice = gTTS(message, lang="ru")
    file_voice_name = '_audio_'+str(time.time())+'_'+str(random.randint(0, 10000))+'.mp3' # создание аудиозаписи
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name) # проигрывание сообщения пользователю
    os.system('del ' + file_voice_name) # удаление исходного аудио
    print('Голосовой ассистент: ' + message) # вывод сообщения в консоль

# здесь реализован GUI но пока что также в тестовом варианте
window = Tk() # окно интерфейса
window['bg'] = 'white'
window.iconbitmap('logo.ico')
window.resizable(False, False)
window.title("Voice assistent Mikki")
window.geometry('400x600'.format(300, 0))
# выше реализованы параметры окошка, в котором пользователь будет совершать действия
imageq = ImageTk.PhotoImage(file="lg1.png")
tapped = ImageTk.PhotoImage(file="microtapped.png")

global pushed_flag
pushed_flag = 0
btn = Button(window, image=imageq, height=100, width=100,
             activebackground='white', command=clicked, borderwidth=0)
btn.place(x=150, y=485)
btn['bg'] = 'white'
textspeech = Text(window, width=45, height=5, borderwidth=1)
textspeech.place(x=10, y = 100)
textmikki = Text(window, width=45, height=5, borderwidth=1)
textmikki.place(x=10, y = 200)
# установка всех конфигураций кнопок, диалоговых окон, всех размеров, цветов,
# картинок и логотипов и подключение реализованного управления голосом
window.mainloop() # запуск окна
a = input('Нажмите Enter..')

