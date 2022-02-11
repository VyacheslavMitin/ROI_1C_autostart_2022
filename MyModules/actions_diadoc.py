# Импорты
import pyautogui as pg
import time
# Импорт моих модулей
from ROI_base import print_log  # мой модуль для вывода времени
from MyModules.select_favorites import selecting_favorites


def actions_1c_diadok():
    """Функция запуска обработки 'Контур.Диадок'."""
    print_log("Запуск автоматизации 'Диадок'", line_before=True)

    selecting_favorites(2)  # контрагенты
    time.sleep(1)
    pg.press('enter')
    time.sleep(15)


if __name__ == '__main__':
    pg.hotkey('alt', 'tab')
    time.sleep(1)
    actions_1c_diadok()
