# Создание столбчатой диаграммы с равномерным значением альфа

На этом этапе мы создадим столбчатую диаграмму, в которой все столбцы имеют одинаковый уровень прозрачности с использованием ключевого аргумента `alpha`.

## Добавление новой ячейки

Добавьте новую ячейку в свой Jupyter Notebook, нажав кнопку "+" в панели инструментов или нажав "Esc", а затем "b" в режиме команд.

## Создание столбчатой диаграммы с равномерным значением альфа

Введите и запустите следующий код в новой ячейке:

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data
x_values = list(range(20))  # 0 to 19
y_values = np.random.randn(20)  # 20 random values from standard normal distribution

# Determine bar colors based on y-values (green for positive, red for negative)
facecolors = ['green' if y > 0 else 'red' for y in y_values]
edgecolors = facecolors  # Same color for edges

# Create the bar chart with alpha=0.5 for all bars
ax.bar(x_values, y_values, color=facecolors, edgecolor=edgecolors, alpha=0.5)

# Add a title and labels
ax.set_title("Bar Chart with Uniform Alpha Value (alpha=0.5)")
ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.show()
```

## Понимание кода и результата

После запуска кода вы должны увидеть столбчатую диаграмму с 20 столбцами. Каждый столбец либо зеленый (положительное значение по оси Y), либо красный (отрицательное значение по оси Y) с одинаковым уровнем прозрачности (альфа = 0.5).

Разберем основные части кода:

1. `np.random.seed(19680801)` - Это гарантирует, что генерируемые случайные числа будут одинаковыми каждый раз, когда вы запускаете код.

2. `x_values = list(range(20))` - Создает список целых чисел от 0 до 19 для оси X.

3. `y_values = np.random.randn(20)` - Генерирует 20 случайных значений из стандартного нормального распределения для оси Y.

4. `facecolors = ['green' if y > 0 else 'red' for y in y_values]` - Эта генерация списка присваивает зеленый цвет положительным значениям и красный - отрицательным.

5. `ax.bar(..., alpha=0.5)` - Основная часть, которая устанавливает равномерное значение альфа, равное 0.5, для всех столбцов.

Равномерное значение альфа делает все столбцы одинаково прозрачными, что может быть полезно, когда вы хотите:

- Показать сетку фона сквозь столбцы
- Создать более нежную визуализацию
- Уравновесить визуальное доминирование всех элементов

На следующем этапе мы рассмотрим, как установить разные значения альфа для разных столбцов.
