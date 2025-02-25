# Отобразите график

После создания и настройки всех текстовых объектов вы можете отобразить график с использованием `plt.show()`. Следующий кодовый блок показывает полный код для графика.

```python
import matplotlib.pyplot as plt

plt.rcParams["font.size"] = 20
ax = plt.figure().add_subplot(xticks=[], yticks=[])

# Первое слово, созданное с использованием text().
text = ax.text(.1,.5, "Matplotlib", color="red")
# Последующие слова, расположенные с использованием annotate(), относительно предыдущего.
text = ax.annotate(
    " says,", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="gold", weight="bold")  # настройки свойства
text = ax.annotate(
    " hello", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="green", style="italic")  # настройки свойства
text = ax.annotate(
    " world!", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="blue", family="serif")  # настройки свойства

plt.show()
```
