# Модуль работы с меню

import pyautogui as pg
# Импорт моих модулей
from ROI_base import *  # мой модуль для вывода времени


def pyautogui_menu() -> str:
    """Функция МЕНЮ"""
    print_log("Запуск меню")

    menu_points = {

        0: "Старт '1С: Бухгалтерия'",
        1: "Старт '1С: Бухгалтерия' - договоры",
        2: "Старт '1С: Бухгалтерия' - Диадок",
        3: "Старт '1С: Бухгалтерия' - выручка",
        4: "Старт '1С: Бухгалтерия' - 014",
        5: "Старт '1С: ВСКК'",
        6: "Старт '1С: ВСКК' - загрузка",

    }
    separator = '=' * 40
    return pg.prompt(text=f"""
    МОДУЛЬ АВТОМАТИЗАЦИИ 1С
    
    Необходимо выбрать пункт меню:

    0: {menu_points.get(0)}
    1: {menu_points.get(1)}
    2: {menu_points.get(2)}
    3: {menu_points.get(3)}
    4: {menu_points.get(4)}
    {separator}
    5: {menu_points.get(5)}
    6: {menu_points.get(6)}
    {separator}
    ESC: выход
    """,
                     title='МЕНЮ АВТОМАТИЗАЦИИ 1С',
                     default='0')


if __name__ == '__main__':
    print(pyautogui_menu())
    print(type(pyautogui_menu()))
