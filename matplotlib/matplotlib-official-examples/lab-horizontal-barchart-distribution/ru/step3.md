# Определение функции

Теперь мы определим функцию под названием `survey`, которая принимает `results` и `category_names` и создает визуализацию горизонтальной накопленной столбчатой диаграммы.

```python
def survey(results, category_names):
    """
    Параметры
    ----------
    results : dict
        Отображение от меток вопросов до списка ответов для каждой категории.
        Предполагается, что все списки содержат одинаковое количество элементов и
        что оно соответствует длине *category_names*.
    category_names : список строк
        Метки категорий.
    """
    # Преобразуем результаты и категории в numpy массивы
    labels = list(results.keys())
    data = np.array(list(results.values()))

    # Вычисляем накопленные суммы данных для горизонтальной накопки
    data_cum = data.cumsum(axis=1)

    # Определяем цвета категорий
    category_colors = plt.colormaps['RdYlGn'](
        np.linspace(0.15, 0.85, data.shape[1]))

    # Создаем график и настраиваем оси
    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    # Создаем накопленные столбцы и добавляем метки столбцов
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color=color)
        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        ax.bar_label(rects, label_type='center', color=text_color)

    # Добавляем легенду
    ax.legend(ncols=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

    return fig, ax
```
