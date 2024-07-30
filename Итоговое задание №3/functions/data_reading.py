try:
    import csv


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
        sales_data = []
        with open(file_path) as file:
            for sale in csv.reader(file):
                sales_data.append(dict(product_name=sale[0],
                                       quantity=int(sale[1]),
                                       price=int(sale[2]),
                                       date=sale[3].strip()))
        return sales_data
except ModuleNotFoundError as e:
    print(e.msg)
