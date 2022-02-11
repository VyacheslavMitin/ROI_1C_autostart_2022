# Импорты
import pyautogui as pg
import time
# Импорт моих модулей
from ROI_base import print_log  # мой модуль для вывода времени
from MyModules.return_tab import return_tab
from MyModules.select_favorites import selecting_favorites


def actions_1c_contracts():
    """Функция отрытия контрагентов и договоров."""
    print_log("Запуск автоматизации 'Клиенты и договоры'", line_before=True)

    selecting_favorites(0)  # контрагенты
    time.sleep(7)
    pg.write('73-000')
    pg.press('enter')
    time.sleep(1)

    selecting_favorites(1)  # договоры
    time.sleep(5)
    pg.write('73-000')
    pg.press('enter')
    time.sleep(1)

    return_tab()


if __name__ == '__main__':
    pg.hotkey('alt', 'tab')
    time.sleep(1)
    actions_1c_contracts()
