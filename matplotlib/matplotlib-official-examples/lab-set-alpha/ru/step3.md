# Создание столбчатой диаграммы с различными значениями альфа

На этом этапе мы будем использовать формат кортежа `(matplotlib_color, alpha)`, чтобы присвоить разный уровень прозрачности каждому столбцу в зависимости от его значений данных.

## Добавление новой ячейки

Добавьте новую ячейку в свой Jupyter Notebook, нажав кнопку "+" в панели инструментов или нажав "Esc", а затем "b" в режиме команд.

## Создание столбчатой диаграммы с различными значениями альфа

Введите и запустите следующий код в новой ячейке:

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data (using the same data as in Step 2 for comparison)
x_values = list(range(20))  # 0 to 19
y_values = np.random.randn(20)  # 20 random values from standard normal distribution

# Determine bar colors based on y-values (green for positive, red for negative)
facecolors = ['green' if y > 0 else 'red' for y in y_values]
edgecolors = facecolors  # Same color for edges

# Calculate alpha values based on the absolute y-values
# Normalize y values to get alpha values between 0.2 and 1.0
abs_y = [abs(y) for y in y_values]
max_abs_y = max(abs_y)
face_alphas = [0.2 + 0.8 * (val / max_abs_y) for val in abs_y]

# Create color-alpha tuples for each bar
colors_with_alphas = list(zip(facecolors, face_alphas))

# Create the bar chart with varying alpha values
ax.bar(x_values, y_values, color=colors_with_alphas, edgecolor=edgecolors)

# Add a title and labels
ax.set_title("Bar Chart with Varying Alpha Values Based on Bar Height")
ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.show()
```

## Понимание кода и результата

После запуска кода вы должны увидеть столбчатую диаграмму с 20 столбцами. Каждый столбец имеет уровень прозрачности, пропорциональный абсолютному значению по оси Y - более высокие столбцы более непрозрачны, более низкие - более прозрачны.

Разберем основные части кода:

1. `abs_y = [abs(y) for y in y_values]` - Это создает список абсолютных значений всех значений по оси Y.

2. `max_abs_y = max(abs_y)` - Находит максимальное абсолютное значение для нормализации данных.

3. `face_alphas = [0.2 + 0.8 * (val / max_abs_y) for val in abs_y]` - Вычисляет значения альфа от 0.2 до 1.0 на основе нормализованных абсолютных значений по оси Y.

4. `colors_with_alphas = list(zip(facecolors, face_alphas))` - Создает список кортежей (цвет, альфа), сопоставляя каждый цвет с соответствующим значением альфа.

5. `ax.bar(..., color=colors_with_alphas, ...)` - Использует кортежи (цвет, альфа) для установки разных значений альфа для каждого столбца.

Подход с использованием различных уровней прозрачности эффективен для:

- Подчеркивания более значимых точек данных
- Сглаживания менее значимых точек данных
- Создания визуальной иерархии на основе значений данных
- Добавления дополнительного измерения информации в визуализацию

Вы можете четко увидеть, как различные значения альфа создают визуальный эффект, при котором величина точки данных подчеркивается как высотой столбца, так и его непрозрачностью.
