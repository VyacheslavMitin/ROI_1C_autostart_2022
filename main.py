# Модуль автоматизации работы в 1С.
# Python 3.8
__author__ = 'Vyacheslav Mitin <vyacheslav.mitin@gmail.com>'
__version__ = '13 - разработка'

# Импорты
import os
import sys
import time
import pyautogui as pg  # установить через pip install pyautogui
# Импорт моих модулей
from ROI_base import print_log  # мой модуль для вывода времени
from MyModules.menu_gui import pyautogui_menu


# ФУНКЦИИ
def welcoming(name_='Автоматизация 1C', author_='Вячеслав Митин', version_='0.1'):
    """Функция приветствия"""
    print(f"МОДУЛЬ РАБОТЫ '{name_}'")
    print(f"Автор модуля: '{author_}'")
    print(f"Версия модуля: '{version_}'\n")


def success_window_alert():
    """Функция отбивки об успехе"""
    time.sleep(1)
    pg.alert("Автоматизация завершена", title="Завершено")
    print_log("Автоматизация завершена", line_before=True)
    sys.exit(0)


def main():
    welcoming()

    select = pyautogui_menu()  # запуск меню
    if select == 0:
        pass
    elif select == 1:
        pass
    elif select == 2:
        pass
    elif select == 3:
        pass
    elif select == 4:
        pass
    elif select == 5:
        pass
    elif select == 6:
        pass

    success_window_alert()


if __name__ == '__main__':
    main()
