def total_sales_per_product(sales_data):
    """
    Функция принимает список продаж и возвращает словарь,
    где ключ - название продукта, а значение - общая сумма продаж этого продукта
    :param sales_data: Список продаж
    :return: Словарь
    """
    sales_products = {}  # Словарь с результатами
    for sale in sales_data:  # Построчный проход по списку продаж
        if sale.get('product_name') in sales_products.keys():  # Проверка на присутсвие значания в списке ключей словаря
            sales_products[sale.get('product_name')] += sale.get('quantity') * sale.get('price')
        else:
            sales_products[sale.get('product_name')] = sale.get('quantity') * sale.get('price')
    return sales_products  # Возвращение словаря
