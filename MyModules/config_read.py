# Модуль чтения конфига с настройками
# from MyModules.config_read import *

import configparser
import os

# КОНСТАНТЫ
windows_1c = ('ТКФ 8.3 Основная 2017',  # кортеж с именами окон 1С и 1С ВСКК
              'Конфигуратор - Бухгалтерия предприятия КОРП, редакция 3.0',
              '[КОПИЯ] ТКФ 8.3 Основная 2017',
              'ЗУП 8.3 Основная / Зарплата и управление персоналом, редакция 3.1',
              'Конфигуратор - Зарплата и управление персоналом, редакция 3.1',
              '[КОПИЯ] ЗУП 8.3 Основная / Зарплата и управление персоналом, редакция 3.1',
              'ВСКК. Рабочая база. / 1С:ERP Управление предприятием 2',
              '63 Самара 1С Бухгалтерия 8.3 ТКФ (ЦОД РОИ)')

name_curdir = os.path.basename(os.path.abspath(os.path.curdir))

if name_curdir == 'MyModules':
    path_ = os.path.abspath(os.path.join(os.path.curdir, '..')) + '\\'
else:
    path_ = os.path.abspath(os.path.join(os.path.curdir)) + '\\'

INI_FILE = 'config.ini'
PATH_TO_INI = path_ + INI_FILE

cfg = configparser.ConfigParser()  # создание объекта с вызовом класса модуля работы с .ini файлами
cfg.read(PATH_TO_INI)

ONEC_BIN = cfg.get('PATHS', 'onec_bin')  # путь к интерактивному клиенту

LOGIN_1C_SAMARA = cfg.get('AUTHORIZATION', 'login_vs151')  # логин и пароль для 1с ВСКК
PASS_1C_SAMARA = cfg.get('AUTHORIZATION', 'pass_vs151')
LOGIN_1C_VSKK = cfg.get('AUTHORIZATION', 'login_vskk')  # логин и пароль для 1с ВСКК
PASS_1C_VSKK = cfg.get('AUTHORIZATION', 'pass_vskk')

SAMARA_SERVER = cfg.get('SERVERS', 'samara_serv')  # имя сервера для SQL
ULYAN_SERVER = cfg.get('SERVERS', 'ulyan_serv')  # имя сервера для SQL
VSKK_URL = cfg.get('SERVERS', 'vskk_url')  # ссылка для ВСКК