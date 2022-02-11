# Функция возврата к первой вкладке
# from MyModules.return_tab import return_tab

# Импорты
import time
import pyautogui as pg
from ROI_base import print_log  # мой модуль для вывода времени


def return_tab(count=2):
    """Функция возврата к первой вкладке в открытой 1С. По умолчанию - 2 раза нажать хоткей."""
    time.sleep(1)

    print_log("Возврат к первой вкладке")
    for y in range(count):  # возврат к первой открытой вкладке
        pg.hotkey('ctrl', 'shift', 'tab')  # через прошагивание вкладок обратным ходом


if __name__ == '__main__':
    pg.hotkey('alt', 'tab')
    time.sleep(1)
    return_tab()
