# Модуль автоматизации работы в 1С.
# Python 3.8
__author__ = 'Vyacheslav Mitin <vyacheslav.mitin@gmail.com>'
__version__ = '13 - разработка'

# Импорты
import pyautogui as pg  # установить через pip install pyautogui
# Импорт моих модулей
from ROI_base import *  # мой модуль для вывода времени
import ROI_common  # мой модуль для создания папок, определения дат, запуска проводника



if __name__ == '__main__':
    ROI_common.making_dirs()  # создание каталогов для отчетов и выгрузок
    main()
