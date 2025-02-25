# Создайте последующие текстовые объекты

Следующим шагом является создание последующих текстовых объектов с использованием `~.Axes.annotate`. Эта функция позволяет вам размещать текстовый объект относительно предыдущего текстового объекта. Следующий код создает три текстовых объекта, которые размещаются справа от предыдущего текстового объекта.

```python
text = ax.annotate(
    " says,", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="gold", weight="bold")  # custom properties
text = ax.annotate(
    " hello", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="green", style="italic")  # custom properties
text = ax.annotate(
    " world!", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="blue", family="serif")  # custom properties
```
