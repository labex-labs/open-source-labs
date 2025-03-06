# Понимание значений альфа в Matplotlib

На этом первом этапе мы создадим Jupyter Notebook и узнаем, как настроить базовую визуализацию с использованием значений альфа.

## Создание первой ячейки Jupyter Notebook

В этой ячейке мы импортируем необходимые библиотеки и создадим два перекрывающихся круга с разными значениями альфа, чтобы продемонстрировать прозрачность.

```python
import matplotlib.pyplot as plt
import numpy as np

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(6, 4))

# Create a circle with alpha=1.0 (completely opaque)
circle1 = plt.Circle((0.5, 0.5), 0.3, color='blue', alpha=1.0, label='Opaque (alpha=1.0)')

# Create a circle with alpha=0.5 (semi-transparent)
circle2 = plt.Circle((0.7, 0.5), 0.3, color='red', alpha=0.5, label='Semi-transparent (alpha=0.5)')

# Add circles to the axes
ax.add_patch(circle1)
ax.add_patch(circle2)

# Set axis limits
ax.set_xlim(0, 1.2)
ax.set_ylim(0, 1)

# Add a title and legend
ax.set_title('Demonstrating Alpha Values in Matplotlib')
ax.legend(loc='upper right')

# Show the plot
plt.show()
```

После того, как вы введете этот код в ячейку, запустите его, нажав Shift+Enter или нажав кнопку "Run" в панели инструментов.

## Понимание результата

Вы должны увидеть два перекрывающихся круга:

- Левый синий круг полностью непрозрачный (альфа = 1.0)
- Правый красный круг полупрозрачный (альфа = 0.5)

Обратите внимание, как вы можете видеть синий круг сквозь красный в месте их пересечения. Это эффект установки значения альфа равным 0.5 для красного круга.

Значения альфа контролируют прозрачность в визуализациях и могут быть полезны в следующих случаях:

- При отображении перекрывающихся точек данных
- При выделении определенных элементов
- При уменьшении визуального шума на плотных графиках
- При создании многослойных визуализаций

Продолжим исследовать больше применений значений альфа на следующем этапе.
