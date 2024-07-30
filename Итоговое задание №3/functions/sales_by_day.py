def sales_over_time(sales_data):
    """
    Функция принимает список продаж и возвращает словарь, где ключ - дата, а значение общая сумма продаж за эту дату
    :param sales_data: Список продаж
    :return: Словарь
    """
    sales_days = {}
    for sale in sales_data:
        if sale.get('date') in sales_days.keys():
            sales_days[sale.get('date')] += sale.get('quantity') * sale.get('price')
        else:
            sales_days[sale.get('date')] = sale.get('quantity') * sale.get('price')
    return sales_days
