import pyautogui as pg  # установить через pip install pyautogui
import subprocess
import sys

# Импорт моих модулей
from ROI_base import print_log  # мой модуль для вывода времени
from MyModules.config_read import *
from MyModules.check_1c_start import check_start_1c


def start_1c_vskk(actions=0):
    """Функция входа в 1С ВСКК."""
    print_log(f"Запуск '1C ВСКК'", line_before=True)

    subprocess.Popen([  # "Запуск '1C' и вход в базу
        ONEC_BIN,  # вызов бинарника 1С
        '/WS', VSKK_URL,  # путь к базе 1С ВСКК
        '/wsn', LOGIN_1C_VSKK, '/wsp', PASS_1C_VSKK  # данные для авторизации в веб-сервер 1С ВСКК
    ])

    if check_start_1c():  # проверка результата функции, True
        if actions == 0:
            pass  # никакой автоматизации ВСКК
        elif actions == 1:
            from MyModules.actions_vskk import actions_1c_vskk
            actions_1c_vskk()  # запуск автоматизации 1С ВСКК

    else:
        print_log("Не удалось запустить 1С ВСКК! Выход с ошибкой!")
        sys.exit(1)


if __name__ == '__main__':
    start_1c_vskk()
