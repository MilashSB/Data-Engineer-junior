try:
    import matplotlib.pyplot as plt  # Импорт библиотеки для построения графиков


    def main():
        """
        Глваная функция, которая осуществляет вывод на экран двух значений и построение двух графиков
        :return: Два значения и два графика
        """
        from .data_reading import read_sales_data  # Импорт функции чтения данных из csv-файла
        from .sales_by_product import total_sales_per_product  # Импорт функции подсчета суммы продаж по продуктам
        from .sales_by_day import sales_over_time  # Импорт функции подсчета продаж суммы по дням

        data = read_sales_data(file_path='sales_data.csv')  # Вызов вышеимпортированной функции
        products = total_sales_per_product(sales_data=data)  # Вызов вышеимпортированной функции
        days = sales_over_time(sales_data=data)  # Вызов вышеимпортированной функции

        fig, (axs1, axs2) = plt.subplots(nrows=1, ncols=2)  # Создание сетки для графиков

        fig.set_figheight(6)  # Задаем высоту графика
        fig.set_figwidth(18)  # Задаем ширину графика

        for product, value in products.items():  # Получение ключей и значений из словаря с продуктами
            if value == max(products.values()):  # Сравнение значения с их максимальной величиной
                print(f'Продукт "{product}" принес наибольшую выручку')  # Вывод название продукта на экран
                # Построение графика по продуктам
                axs1.plot(products.keys(),
                          products.values(),
                          label=f'Продукт "{product}" принес наибольшую выручку',
                          color='green',
                          linewidth=3,
                          linestyle='-',
                          marker='o',
                          markersize=6,
                          markerfacecolor='yellow')
                axs1.grid(color='red',
                          linestyle='--',
                          linewidth=0.318)
                axs1.legend(loc='lower right')
                axs1.set_title(label='График общей суммы продаж по каждому продукту',
                               fontsize=18,
                               fontweight='bold',
                               pad=18)
                axs1.set_xlabel(xlabel='Продукт',
                                fontsize=18)
                axs1.set_ylabel(ylabel='Сумма',
                                fontsize=18)

        for day, value in days.items():  # Получение ключей и значений из словаря с датами
            if value == max(days.values()):  # Сравнение значения с их максимальной величиной
                print(f'В день "{day}" была наибольшая сумма продаж')  # Вывод даты на экран
                # Построение графика по дням
                axs2.plot(days.keys(),
                          days.values(),
                          label=f'В день "{day}" была наибольшая сумма продаж',
                          color='blue',
                          linewidth=3,
                          linestyle='-',
                          marker='s',
                          markersize=6,
                          markerfacecolor='yellow')
                axs2.grid(color='red',
                          linestyle='--',
                          linewidth=0.318)
                axs2.legend(loc='lower right')
                axs2.set_title(label='График общей суммы продаж по дням',
                               fontsize=18,
                               fontweight='bold',
                               pad=18)
                axs2.set_xlabel(xlabel='День',
                                fontsize=18)
                axs2.set_ylabel(ylabel='Сумма',
                                fontsize=18)

        plt.get_current_fig_manager().set_window_title('Графики')  # Название окна с графиками
        plt.tight_layout()  # Автоподбор отступов между графиками в зависимости от размеров сетки
        plt.show()  # Вывод графиков на экран
except ModuleNotFoundError as e:  # Отлавливание ошибок при импорте файлов
    print(e.msg)  # Вывод текста ошибки
except ImportError as e:  # Отлавливание ошибок при импорте функций
    print(e.msg.split('(')[0])  # Вывод текста ошибки
