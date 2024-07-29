def sales_over_time(sales_data):
    """
    Функция принимает список продаж и возвращает словарь, где ключ - дата, а значение общая сумма продаж за эту дату
    :param sales_data: Список продаж
    :return: Словарь
    """
    sales_days = {}  # Словарь с результатами
    for sale in sales_data:  # Построчный проход по списку продаж
        if sale.get('date') in sales_days.keys():  # Проверка на присутсвие значания в списке ключей словаря
            sales_days[sale.get('date')] += sale.get('quantity') * sale.get('price')
        else:
            sales_days[sale.get('date')] = sale.get('quantity') * sale.get('price')
    return sales_days  # Возвращение словаря
