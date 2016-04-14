__author__ = 'pridachin'
import os
import shutil


# Сканирование директории источника
def scan_dir(dirname_source):
    list_files = []  # список локальных путей с именами файлов в корневом каталоге
    # Цикл для поиска всех файлов в каталоге dirname_source
    for (curr_dir, sub_dirs, files) in os.walk(dirname_source):
        # Цикл для формирования списка списка локальных путей файлов в каталоге dirname_source
        for file in files:
            buf_path = curr_dir.replace(dirname_source, '')  # Удаление глобальной части в пути файла без имени файла
            local_path = os.path.join(buf_path, file)  # формирование локального пути до файла с именем файла
            list_files.append(local_path)  # добавление локального пути до файла в список локальных путей
    return list_files


# Копирование файлов из директори источника в директорию назначения
def copy_files(list_files, dirname_source, dirname_dest):
    # Цикл по локальным путям файлов в списке локальных путей для копирования
    col_copied_files = 0
    for file in list_files:
        path_s = dirname_source + '\\' + file  # Формирование глобального пути до файла источника
        path_d = dirname_dest + '\\' + file  # Формирование глобального пути до файла назначения
        # Проверка условия "если в каталоге не существует подкаталога"
        # file.split('\\')[-1] возвращает имя файла с расширением в последнем подкаталоге например file.txt
        if not os.path.exists(path_d.replace(file.split('\\')[-1], '')):
            os.makedirs(path_d.replace(file.split('\\')[-1], ''))  # создание подкаталога
        if not os.path.exists(path_d):
            shutil.copyfile(path_s, path_d)  # копирование файла
            col_copied_files += 1
    print('Скопировано файлов: ' + str(col_copied_files))


# Копирование файлов из директори источника в директорию назначения, с заменой файлов
def replace_files(list_files, dirname_source, dirname_dest):
    # Цикл по локальным путям файлов в списке локальных путей для копирования
    col_copied_files = 0
    for file in list_files:
        path_s = dirname_source + '\\' + file  # Формирование глобального пути до файла источника
        path_d = dirname_dest + '\\' + file  # Формирование глобального пути до файла назначения
        # Проверка условия "если в каталоге не существует подкаталога"
        # file.split('\\')[-1] возвращает имя файла с расширением в последнем подкаталоге например file.txt
        if not os.path.exists(path_d.replace(file.split('\\')[-1], '')):
            os.makedirs(path_d.replace(file.split('\\')[-1], ''))  # создание подкаталога
        shutil.copyfile(path_s, path_d)  # копирование файла
        col_copied_files += 1
    print('Скопировано файлов: ' + str(col_copied_files))