# Модуль работы с меню "робот" в ИТКО
# from MyModules.select_favorites import selecting_favorites
import time
import pyautogui as pg


def selecting_favorites(point):
    """Функция выбора строки меню в 'Избранном'.
    0 - Контрагенты
    1 - Договоры
    2 - Доп. обработки ДИАДОК
    3 - Реализация (акты, накладные, УПД)
    4 - Счета покупателям
    5 - Дополнительные отчеты СВОД
    6 - Загрузка 014
    7 - Оборотно-сальдовая ведомость по счету"""

    timeout = 1  # без таймаута
    for item in range(3):
        time.sleep(0.5)
        pg.hotkey('ctrl', 'shift', 'b')  # вызов меню избранного 1С

    time.sleep(5)

    pg.press('down', presses=point, interval=timeout)
    time.sleep(timeout)
    pg.press('enter')
    time.sleep(timeout)


if __name__ == '__main__':
    pg.hotkey('alt', 'tab')
    time.sleep(1)
    selecting_favorites(7)
