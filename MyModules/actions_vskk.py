# Импорты
import pyautogui as pg
import time
# Импорт моих модулей
from ROI_base import *  # мой модуль для вывода времени
import ROI_common  # мой модуль для создания папок, определения дат, запуска проводника


def actions_1c_vskk():
    """Функция работы в '1С ВСКК'."""
    time.sleep(5)
    print_log("Запуск автоматизации работы с 1С ВСКК", line_before=True)
    while True:
        print_log("Поиск окна 1С ВСКК...")  # поиск окон основной базы и копии 1С ВСКК
        original = 'ВСКК. Рабочая база. / 1С:ERP Управление предприятием 2'  # имя боевой базы ВСКК
        if original in pg.getAllTitles():  # поиск окна
            print_log(f"Обнаружено окно '{original}'")
            pg.getWindowsWithTitle(original)[0].activate()  # активация окна
            start_date, finish_date, *_ = ROI_common.past_dates()  # подстановка дат прошлого месяца
            break  # выход из цикла
        time.sleep(10)
    count = 0  # считать шаги, чтобы дергать разные меню и по разному реагировать на них
    for menus in range(count, 4):  # в цикле открывать вкладки из меню избранного 1С ВСКК 0-3
        time.sleep(10)
        pg.hotkey('ctrl', 'shift', 'b')  # вызов меню избранного 1С ВСКК
        time.sleep(3)
        pg.press('down', presses=count)  # спуск до нужного меню в избранном основываясь на счетчике
        print_log(f"Меню - 0{count}")  # печать текущего шага цикла в переборе меню избранного 1С
        time.sleep(1)
        pg.press('enter')  # вход в меню в избранном
        if count == 0:  # работа с меню "РОИ Точки обслуживания"
            time.sleep(2)
            pg.press('tab', presses=7, interval=0.5)  # переход в поле выбора филиала
            time.sleep(1)
            pg.write('1')  # костыльный способ вызвать "Ульяновский филиал" для выбора
            time.sleep(1)
            pg.press('down')  # выбор Ульяновского филиала
            time.sleep(1)
            pg.press('enter')  # выбор Ульяновского филиала
            time.sleep(1)
        if count == 2:  # работа с меню "Оказанные услуги"
            time.sleep(2)
            pg.press('tab', presses=10)  # переход на кнопку "ЕЩЕ"
            time.sleep(1)
            pg.press('down', presses=6)  # спуск до меню "Установить период"
            time.sleep(1)
            pg.press('enter')  # вход в меню "Установить период"
            pg.write(start_date, interval=0.3)  # подстановка даты начала предыдущего месяца
            pg.press('tab')
            pg.write(finish_date, interval=0.3)  # подстановка даты окончания предыдущего месяца
            pg.press('enter', presses=2)  # подтверждение даты периода
        count += 1
    return_first_tab(1)  # возврат к первой открытой вкладке, значение не по умолчанию
