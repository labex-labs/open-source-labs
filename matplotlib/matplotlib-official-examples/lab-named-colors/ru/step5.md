# Создание столбчатой диаграммы

Мы также можем использовать Matplotlib для создания столбчатой диаграммы. В этом примере мы создадим столбчатую диаграмму, которая покажет количество проданных яблок, бананов и апельсинов.

```python
import matplotlib.pyplot as plt

# данные для построения
apples = 10
bananas = 15
oranges = 5

# создание столбчатой диаграммы
plt.bar(["Apples", "Bananas", "Oranges"], [apples, bananas, oranges])

# установка заголовка
plt.title("Simple Bar Plot")

# установка метки оси x
plt.xlabel("Fruits")

# установка метки оси y
plt.ylabel("Quantity")

# отображение диаграммы
plt.show()
```
