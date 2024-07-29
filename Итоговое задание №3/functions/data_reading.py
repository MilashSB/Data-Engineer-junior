try:
    import csv  # Импорт библиотеки для чтения csv-файлов


    def read_sales_data(file_path):
        """
        Функция принимает путь к csv-файлу и возвращает список продаж
        :param file_path: Путь к csv-файлу
        :return: Продажи в свою очередь являются словарями с ключами:
         product_name (название),
         quantity (количество),
         price (цена),
         date (дата)
        """
        sales_data = []  # Итоговый список
        with open(file_path) as file:  # Открытие файла для чтения
            for sale in csv.reader(file):  # Считывание данных из файла построчно
                sales_data.append(dict(product_name=sale[0],
                                       quantity=int(sale[1]),
                                       price=int(sale[2]),
                                       date=sale[3].strip()))  # Добавление данных в список продаж
        return sales_data  # Возвращение списка продаж
except ModuleNotFoundError as e:  # Отлавливание ошибки при импорте библиотеки
    print(e.msg)  # Вывод текста ошибки
