# Создание комбинированной визуализации с использованием различных методов настройки прозрачности (альфа-значений)

На этом последнем этапе мы объединим несколько методов для создания более сложной визуализации, которая демонстрирует как одинаковые, так и переменные значения прозрачности (альфа-значения) на одном графике.

## Добавление новой ячейки

Добавьте новую ячейку в свой Jupyter Notebook, нажав кнопку "+" в панели инструментов или нажав "Esc", а затем "b" в режиме команд.

## Создание комбинированной визуализации

Введите и запустите следующий код в новой ячейке:

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Generate some common data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

# First subplot: Fixed alpha for all lines
ax1.plot(x, y1, color='red', linewidth=2, label='sin(x)', alpha=0.7)
ax1.plot(x, y2, color='blue', linewidth=2, label='cos(x)', alpha=0.7)
ax1.plot(x, y3, color='green', linewidth=2, label='sin(x)cos(x)', alpha=0.7)

# Add title and legend to first subplot
ax1.set_title("Multiple Lines with Uniform Alpha")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.5)

# Second subplot: Scatter plot with varying alpha based on y-value
sizes = np.abs(y3 * 100) + 10  # Vary point sizes based on y3
colors = y3  # Use y3 values for coloring

# Calculate varying alpha values between 0.3 and 1.0 based on absolute y3 values
alphas = 0.3 + 0.7 * (np.abs(y3) / max(np.abs(y3)))

# Create a scatter plot with varying sizes, colors, and alphas
scatter = ax2.scatter(x, y3, s=sizes, c=colors, cmap='viridis',
                     alpha=alphas)

# Add title and labels to second subplot
ax2.set_title("Scatter Plot with Varying Alpha Based on Y-Value")
ax2.set_xlabel("x")
ax2.set_ylabel("sin(x)cos(x)")
ax2.grid(True, linestyle='--', alpha=0.5)

# Add a colorbar to the second subplot
cbar = plt.colorbar(scatter, ax=ax2)
cbar.set_label('Value of sin(x)cos(x)')

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
```

## Понимание кода и результата

После запуска кода вы должны увидеть фигуру с двумя подграфиками, расположенными рядом друг с другом:

1. **Левый подграфик (одинаковая прозрачность)**: Показывает три тригонометрические функции, построенные с одинаковым значением прозрачности (альфа = 0.7).

2. **Правый подграфик (переменная прозрачность)**: Показывает точечную диаграмму, где:
   - Координата x - это входное значение.
   - Координата y - это sin(x)cos(x).
   - Размер каждой точки изменяется в зависимости от абсолютного значения y.
   - Цвет каждой точки изменяется в зависимости от значения y.
   - Прозрачность (альфа) каждой точки изменяется в зависимости от абсолютного значения y.

Разберём основные части кода:

1. `fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))` - Создает фигуру с двумя подграфиками, расположенными рядом друг с другом.

2. Для первого подграфика:

   - `ax1.plot(..., alpha=0.7)` - Использует одинаковое значение прозрачности для всех трех линий.

3. Для второго подграфика:
   - `alphas = 0.3 + 0.7 * (np.abs(y3) / max(np.abs(y3)))` - Вычисляет переменные значения прозрачности в диапазоне от 0.3 до 1.0.
   - `ax2.scatter(..., alpha=alphas)` - Использует переменные значения прозрачности для точек точечной диаграммы.

Это сочетание методов демонстрирует, как значения прозрачности (альфа-значения) могут быть использованы различными способами для улучшения визуализаций:

- **Одинаковая прозрачность** полезна, когда вам нужно показать несколько перекрывающихся элементов с равной важностью.

- **Переменная прозрачность** полезна, когда вы хотите подчеркнуть определенные точки данных в зависимости от их значений.

Освоив эти методы, вы сможете создавать более эффективные и визуально привлекательные визуализации данных.
