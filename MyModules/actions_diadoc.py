# Импорты
import pyautogui as pg
import time
# Импорт моих модулей
from ROI_base import *  # мой модуль для вывода времени
import ROI_common  # мой модуль для создания папок, определения дат, запуска проводника


def actions_1c_diadok():
    """Функция запуска внешней обработки 'Контур.Диадок' в '1С Бухгалтерия'."""
    *_, path = ROI_common.return_path_dirs()  # переменная для года и месяца (2021\04 Apr), для вставки текста
    time.sleep(5)
    print_log("Запуск автоматизации 'Контур.Диадок'", line_before=True)
    while True:
        print_log("Поиск окна 1С...")  # поиск окон основной базы и копии 1С Бух
        original = 'ТКФ 8.3 Основная 2017'  # имя боевой базы
        copy = '[КОПИЯ] ТКФ 8.3 Основная 2017'  # имя копии
        if copy in pg.getAllTitles():  # поиск окна
            print_log(f"Обнаружено окно '{copy}'")
            pg.getWindowsWithTitle(copy)[0].activate()  # активация окна
            start_date, finish_date, *_ = ROI_common.current_dates()  # подстановка дат текущего месяца
            break  # выход из цикла
        if original in pg.getAllTitles():  # поиск окна
            print_log(f"Обнаружено окно '{original}'")
            pg.getWindowsWithTitle(original)[0].activate()  # активация окна
            start_date, finish_date, *_ = ROI_common.past_dates()  # подстановка дат прошлого месяца
            break
        time.sleep(10)
    for times in range(5):  # закрытие само открывающихся вкладок 1С
        time.sleep(1)
        pg.hotkey('ctrl', 'f4')
    count = 5  # считать шаги, чтобы дергать разные меню и по разному реагировать на них
    for menus in range(count, 7):  # в цикле открывать вкладки из меню избранного 1С (только для бухгалтерии) 0-3
        time.sleep(10)  # очень не стабильно работает сама 1С, нужны большие временные лаги
        pg.hotkey('ctrl', 'shift', 'b')  # вызов меню избранного 1С
        time.sleep(7)
        pg.press('down', presses=count)  # спуск до нужного меню в избранном основываясь на счетчике
        print_log(f"Меню - 0{count}")  # печать текущего шага цикла в переборе меню избранного 1С
        time.sleep(2)
        pg.press('enter')  # вход в меню в избранном
        if count == 5:  # работа с меню "Дополнительные обработки"
            time.sleep(5)
            pg.press('enter')  # запуск Контур.Диадок
            print_log("Запуск доп. обработки 'Контур.Диадок'")
            time.sleep(10)
            pg.hotkey('ctrl', 'tab')  # через прошагивание вкладок обратным ходом
            time.sleep(1)
            pg.hotkey('ctrl', 'f4')
            print_log("Закрытие вкладки с дополнительными обработками")
        if count == 6:  # работа с меню "Контрагенты"
            time.sleep(15)  # ожидание долгой отрисовки журнала контрагентов
        count += 1
    return_first_tab()  # возврат к первой открытой вкладке

