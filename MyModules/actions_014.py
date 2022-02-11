# Импорты
import pyautogui as pg
import time
# Импорт моих модулей
from ROI_base import print_log  # мой модуль для вывода времени
from MyModules.return_tab import return_tab
from MyModules.select_favorites import selecting_favorites


def actions_014():
    """Функция 014"""
    print_log("Запуск автоматизации '014'", line_before=True)

    selecting_favorites(6)
    selecting_favorites(7)

    return_tab()


if __name__ == '__main__':
    pg.hotkey('alt', 'tab')
    time.sleep(1)
    actions_014()
