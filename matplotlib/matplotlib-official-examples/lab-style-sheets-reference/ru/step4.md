# Построить демонстрационный рисунок для каждого стиля оформления

Наконец, вам нужно построить демонстрационный рисунок для каждого доступного стиля оформления. Вы можете сделать это, пройдя в цикле по `style_list` и вызвав функцию `plot_figure()` для каждого стиля оформления.

```python
if __name__ == "__main__":

    # Создайте список всех доступных стилей, в алфавитном порядке, но
    # `default` и `classic` будут располагаться соответственно в
    # первой и второй позиции.
    # Стили с ведущими подчеркиваниями предназначены для внутреннего использования, таких как тестирование
    # и галерея типов графиков. Они здесь исключаются.
    style_list = ['default', 'classic'] + sorted(
        style for style in plt.style.available
        if style!= 'classic' and not style.startswith('_'))

    # Постройте демонстрационный рисунок для каждого доступного стиля оформления.
    for style_label in style_list:
        with plt.rc_context({"figure.max_open_warning": len(style_list)}):
            with plt.style.context(style_label):
                plot_figure(style_label=style_label)

    plt.show()
```
