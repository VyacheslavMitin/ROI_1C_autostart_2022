import pyautogui as pg  # установить через pip install pyautogui
import subprocess
import sys

# Импорт моих модулей
from ROI_base import *  # мой модуль для вывода времени
import ROI_common  # мой модуль для создания папок, определения дат, запуска проводника
from MyModules.config_read import *
from MyModules.check_1c_start import check_start_1c


def start_1c(mode='ENTERPRISE', type_bases='/S', server_1c='vs151', path_bases='BUH-KORP-63', actions='0'):
    """Функция входа в программы 1С (кроме ВСКК)."""
    print_log(f"Запуск '1C' c выбранным режимом", line_before=True)

    subprocess.Popen([  # "Запуск '1C' и вход в базу
        ONEC_BIN,  # вызов бинарника 1С - толстого клиента
        mode,  # 'ENTERPRISE', 'CONFIG' - mode, режим работы 1С, по умолчанию Предприятие
        type_bases,  # '/F' - файловая база, '/S' - SQL, тип базы, по умолчанию SQL
        path_bases,  # путь к базе, по умолчанию SQL 'TKF2020'
        '/N', login_1c, '/P', pass_1c  # данные для логина и авторизации
    ])

    if check_start_1c():  # проверка результата функции, True
        if actions == '0':  # ничего не делать
            pass
        elif actions == '1':  #
            pass
        elif actions == '2':  #
            pass
        elif actions == '3':  #
            pass
        elif actions == '+':  #
            pass

        print_log("Выход из модуля", line_before=True, line_after=True)
        pg.alert(f"'1C' в режиме {mode} {type_bases} {path_bases} {actions}\n"
                 f"отработала!\nВремя {datetime.now().strftime('%H-%M')}",
                 title=f'1C {mode} {path_bases}', button='OK')  # окно об успехе

    else:  # проверка результата функции, False
        print_log("Не удалось запустить 1С! Выход с ошибкой!")
        sys.exit(1)
