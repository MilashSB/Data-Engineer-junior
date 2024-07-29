try:
    from functions.data_output import main  # Импорт главной функции

    if __name__ == '__main__':
        main()  # Вызов главной функции
except ModuleNotFoundError as e:  # Отлавливание ошибок при импорте файлов
    print(e.msg)  # Вывод текста ошибки
except ImportError as e:  # Отлавливание ошибок при импорте функций
    print(e.msg.split('(')[0])  # Вывод текста ошибки
except FileNotFoundError as e:  # Отлавливание ошибок при отсутствии csv-файла
    print(f"{e.strerror}: '{e.filename}'")  # Вывод текста ошибки
