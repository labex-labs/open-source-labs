# Использование стиля кода вспомогательной функции

Мы создадим функцию, которая будет принимать данные и метки строк и столбцов в качестве входных параметров и позволять задавать аргументы для настройки графика. Мы отключим наружные линии осей и создадим сетку белых линий для разделения ячеек. Здесь мы также хотим создать цветовую шкалу и расположить метки выше тепловой карты, а не ниже нее. Аннотации должны иметь разные цвета в зависимости от порога для лучшего контраста с цветом пикселя.

```python
def heatmap(data, row_labels, col_labels, ax=None, cbar_kw=None, cbarlabel="", **kwargs):
    """
    Создайте тепловую карту из двумерного массива numpy и двух списков меток.

    Параметры
    ----------
    data
        Двумерный массив numpy размером (M, N).
    row_labels
        Список или массив длиной M с метками для строк.
    col_labels
        Список или массив длиной N с метками для столбцов.
    ax
        Экземпляр `matplotlib.axes.Axes`, на который будет нарисована тепловая карта. Если не указан, используется текущая ось или создается новая. Необязательный.
    cbar_kw
        Словарь с аргументами для `matplotlib.Figure.colorbar`. Необязательный.
    cbarlabel
        Метка для цветовой шкалы. Необязательный.
    **kwargs
        Все остальные аргументы передаются в `imshow`.
    """

    if ax is None:
        ax = plt.gca()

    if cbar_kw is None:
        cbar_kw = {}

    # Нарисуйте тепловую карту
    im = ax.imshow(data, **kwargs)

    # Создайте цветовую шкалу
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # Показать все деления и подписать их соответствующими записями из списка.
    ax.set_xticks(np.arange(data.shape[1]), labels=col_labels)
    ax.set_yticks(np.arange(data.shape[0]), labels=row_labels)

    # Пусть горизонтальные метки делений появляются сверху.
    ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)

    # Поверните метки делений и задайте их выравнивание.
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right", rotation_mode="anchor")

    # Отключите линии обводки и создайте белую сетку.
    ax.spines[:].set_visible(False)
    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar


def annotate_heatmap(im, data=None, valfmt="{x:.2f}", textcolors=("black", "white"), threshold=None, **textkw):
    """
    Функция для аннотации тепловой карты.

    Параметры
    ----------
    im
        AxesImage, который нужно подписать.
    data
        Данные, используемые для аннотации. Если None, используются данные изображения. Необязательный.
    valfmt
        Формат аннотаций внутри тепловой карты. Это должно быть либо строкой форматирования, например, "$ {x:.2f}", либо `matplotlib.ticker.Formatter`. Необязательный.
    textcolors
        Пара цветов. Первый используется для значений ниже порога, второй для значений выше порога. Необязательный.
    threshold
        Значение в единицах данных, по которому применяются цвета из textcolors. Если None (по умолчанию), используется середина цветовой карты в качестве разделителя. Необязательный.
    **kwargs
        Все остальные аргументы передаются в каждый вызов `text`, используемый для создания текстовых меток.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Нормализуйте порог к цветовому диапазону изображения.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # Задайте стандартное выравнивание по центру, но позволяет переопределить его textkw.
    kw = dict(horizontalalignment="center", verticalalignment="center")
    kw.update(textkw)

    # Получите форматтер, если передана строка
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Переберите данные и создайте `Text` для каждого "пикселя".
    # Измените цвет текста в зависимости от данных.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts
```
