# Импорты
import pyautogui as pg
import time
# Импорт моих модулей
from ROI_base import *  # мой модуль для вывода времени
import ROI_common  # мой модуль для создания папок, определения дат, запуска проводника


def actions_1c_contracts():
    """Функция """
    time.sleep(5)
    print_log("Запуск автоматизации 'Подготовка к выручке'", line_before=True)
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
    for times in range(5):  # закрытие самооткрывающихся вкладок 1С
        time.sleep(1)
        pg.hotkey('ctrl', 'f4')
    count = 0  # считать шаги, чтобы дергать разные меню и по разному реагировать на них
    for menus in range(count, 4):  # в цикле открывать вкладки из меню избранного 1С (только для бухгалтерии) 0-3
        time.sleep(10)  # очень не стабильно работает сама 1С, нужны большие временные лаги
        pg.hotkey('ctrl', 'shift', 'b')  # вызов меню избранного 1С
        time.sleep(7)
        pg.press('down', presses=count)  # спуск до нужного меню в избранном основываясь на счетчике
        print_log(f"Меню - 0{count}")  # печать текущего шага цикла в переборе меню избранного 1С
        time.sleep(2)
        pg.press('enter')  # вход в меню в избранном
        if count == 0 or count == 3:  # в цикле проверка определенных вкладок, где требуется заполнение дат
            time.sleep(1)
            pg.write(start_date, interval=0.1)  # ввод начальной даты
            pg.press('tab')  # ввод переход в другое поле
            time.sleep(1)
            pg.write(finish_date, interval=0.1)  # ввод конечной даты
            if count == 0:  # в цикле заполнение конечной даты три раза в трех полях
                pg.press('tab', presses=2)
                time.sleep(1)
                pg.write(finish_date, interval=0.1)
                for i in range(2):  # в цикле раскидывание окончательной даты месяца в цикле во все строки
                    pg.press('tab')
                    time.sleep(1)
                    pg.write(finish_date, interval=0.1)
                pg.press('tab')  # выбор чекбокса типа файла импорта
                time.sleep(1)
                pg.press('right')  # выбор формата файла TXT
                pg.press('tab')  # переход в поле выбора подразделения
                time.sleep(1)
                pg.write('1')  # костыльный способ вызвать подразделение для выбора
                time.sleep(1)
                pg.press('down')  # выбор подразделения
                time.sleep(1)
                pg.press('enter')  # выбор подразделения
                time.sleep(1)
                pg.hotkey('shift', 'tab')  # возврат в поле выбора подразделения
        count += 1
    return_first_tab()  # возврат к первой открытой вкладке
