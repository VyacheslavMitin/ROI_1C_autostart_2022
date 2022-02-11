# Импорты
import pyautogui as pg
import time
# Импорт моих модулей
from ROI_base import print_log  # мой модуль для вывода времени
from MyModules.return_tab import return_tab
from MyModules.select_favorites import selecting_favorites


def actions_revenue():
    """Функция """
    print_log("Запуск автоматизации 'Подготовка к выручке'", line_before=True)

    selecting_favorites(3)
    selecting_favorites(4)
    selecting_favorites(5)
    time.sleep(1)
    pg.press('enter')

    return_tab()  # возврат к первой открытой вкладке


if __name__ == '__main__':
    pg.hotkey('alt', 'tab')
    time.sleep(1)
    actions_revenue()
