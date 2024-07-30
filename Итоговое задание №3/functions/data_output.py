try:
    import matplotlib.pyplot as plt


    def main():
        """
        Глваная функция, которая осуществляет вывод на экран двух значений и построение двух графиков
        :return: Два значения и два графика
        """
        from .data_reading import read_sales_data
        from .sales_by_product import total_sales_per_product
        from .sales_by_day import sales_over_time

        data = read_sales_data(file_path='sales_data.csv')
        products = total_sales_per_product(sales_data=data)
        days = sales_over_time(sales_data=data)

        fig, (axs1, axs2) = plt.subplots(nrows=1, ncols=2)
        fig.set_figheight(6)
        fig.set_figwidth(18)

        for product, value in products.items():
            if value == max(products.values()):
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

        for day, value in days.items():
            if value == max(days.values()):
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

        plt.get_current_fig_manager().set_window_title('Графики')
        plt.tight_layout()
        plt.show()
except ModuleNotFoundError as e:
    print(e.msg)
except ImportError as e:
    print(e.msg.split('(')[0])
