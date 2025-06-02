#print('абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.upper())



# функция скачивания библеотек
def import_plys(lib_import, lib):
    try:
        exec(f'{lib_import}')
    except:
        try:
            system(f'pip install {lib}')
        except:
            from os import system
            system(f'pip install {lib}')
        finally:
            try:
                exec(f'{lib_import}')
            except:
                try:
                    system(f'pip3 install {lib}')
                    exec(f'{lib_import}')
                except:
                    try:
                        system(f'pip install --user {lib}')
                        exec(f'{lib_import}')
                    except:
                        try:system('python.exe -m pip install --upgrade pip')
                        except:print('error 1')

# Импортируем библеотеки
try:from pygetwindow import getWindowsWithTitle, getAllTitles
except:import_plys('from pygetwindow import getWindowsWithTitle, getAllTitles','pygetwindow')
try:from glob import glob
except:import_plys('from glob import glob','glob')
try:from requests import get
except:import_plys('from requests import get',"requests")
from pygetwindow import getWindowsWithTitle, getAllTitles
from requests import get
from socket import gethostname
from time import time as tm
print(1)



#получаем данные о блокеровках
blok_data = str(get('https://raw.githubusercontent.com/boingo0/sssss/refs/heads/main/hg').text).split('&#&')
bloks = blok_data[1:]
bloks_data = blok_data[0]
print(2)
#главный цикл
update_key = 2
while 1:
    blok_data = str(get('https://raw.githubusercontent.com/boingo0/sssss/refs/heads/main/hg').text).split('&#&')
    for i in range(10):
        bloks = blok_data[1:]
        bloks_data = blok_data[0]
        print(bloks_data)
        #Часть отвечаючея за блокеровку
        if bloks_data[0] == "1":
            try:
                # Получаем данные о окнах
                r = getAllTitles()
                # Отчищяем данные
                for t in r:
                    if '' in r: del r[r.index('')]
                print(r)
                # Блокируем окна
                for win in r:
                    for blok in bloks:
                        # Проверяем наличее тега на игнорирования больших букв
                        if blok[-1] == '%':
                            blok = blok[:-1]
                            win = win.lower()
                            blok = blok.lower()
                        # Проверяем наличее тега на игнорирования точного совподения
                        if blok[0] == '*':
                            blok = blok[1:]
                            # Блокируем окна через in
                            if blok in win:
                                notepadWindow = getWindowsWithTitle(win)[0]
                                notepadWindow.close()
                        else:
                            # Блокируем окна
                            if blok == win:
                                notepadWindow = getWindowsWithTitle(win)[0]
                                notepadWindow.close()
            except IndexError: pass
