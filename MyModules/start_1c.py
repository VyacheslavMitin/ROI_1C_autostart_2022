import pyautogui as pg  # установить через pip install pyautogui
import subprocess
import sys

# Импорт моих модулей
from ROI_base import print_log  # мой модуль для вывода времени
from MyModules.config_read import *
from MyModules.check_1c_start import check_start_1c


def start_1c(

        mode='ENTERPRISE',
        type_bases='/S',
        server_1c=SAMARA_SERVER,
        base_1c=SAMARA_BASE,
        login_1c=LOGIN_1C_SAMARA,
        pass_1c=PASS_1C_SAMARA,
        actions='0'

):

    """Функция входа в программы 1С (кроме ВСКК)."""
    print_log(f"Запуск '1C' c выбранным режимом", line_before=True)

    subprocess.Popen([  # "Запуск '1C' и вход в базу
        ONEC_BIN,  # вызов бинарника 1С - толстого клиента
        mode,  # 'ENTERPRISE', 'CONFIG' - mode, режим работы 1С, по умолчанию Предприятие
        type_bases,  # '/F' - файловая база, '/S' - SQL, тип базы, по умолчанию SQL
        server_1c + '/' + base_1c,  # путь к базе
        '/N', login_1c, '/P', pass_1c  # данные для логина и авторизации
    ])

    if check_start_1c():  # проверка результата функции, True
        if actions == '0':  # ничего не делать
            pass
        elif actions == '1':  #
            pass
        elif actions == '2':  #
            pass
        elif actions == '3':  #
            pass
        elif actions == '+':  #
            pass

    else:  # проверка результата функции, False
        print_log("Не удалось запустить 1С! Выход с ошибкой!")
        sys.exit(1)


if __name__ == '__main__':
    start_1c()
