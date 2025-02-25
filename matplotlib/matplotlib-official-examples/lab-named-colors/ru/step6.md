# Создание круговой диаграммы

Мы также можем использовать Matplotlib для создания круговой диаграммы. В этом примере мы создадим круговую диаграмму, которая покажет процент людей, которые предпочитают разные виды пиццы.

```python
import matplotlib.pyplot as plt

# данные для построения
sizes = [30, 40, 10, 20]
labels = ["Pepperoni", "Mushroom", "Onion", "Sausage"]

# создание круговой диаграммы
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# установка заголовка
plt.title("Simple Pie Chart")

# отображение диаграммы
plt.show()
```
