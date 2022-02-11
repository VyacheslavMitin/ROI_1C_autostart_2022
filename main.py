# Модуль автоматизации работы в 1С.
# Python 3.8

# Импорты
import sys
import time
import pyautogui as pg  # установить через pip install pyautogui
# Импорт моих модулей
from ROI_base import print_log  # мой модуль для вывода времени
from MyModules.menu_gui import pyautogui_menu


# ФУНКЦИИ
def welcoming(name_='Автоматизация 1C', author_='Вячеслав Митин', version_='2.0'):
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

    start_1c, start_1c_vskk = None, None
    if select in ('0', '1', '2', '3', '4',):
        from MyModules.start_1c import start_1c
    elif select in ('5', '6',):
        from MyModules.start_1c_vskk import start_1c_vskk
    else:
        print_log("Выход без действия")
        sys.exit(0)

    if select == '0':
        start_1c()
    elif select == '1':
        start_1c(actions='1')
    elif select == '2':
        start_1c(actions='2')
    elif select == '3':
        start_1c(actions='3')
    elif select == '4':
        start_1c(actions='4')
    elif select == '5':
        start_1c_vskk()
    elif select == '6':
        pass

    success_window_alert()


if __name__ == '__main__':
    main()
