# Настройка графика

Matplotlib предлагает широкий спектр параметров настройки графиков. Вот пример кода, который настраивает наш простой линейный график:

```python
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a plot
plt.plot(x, y, color='red', linewidth=2, linestyle='--', marker='o', markersize=8, markerfacecolor='yellow')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Customized Plot')

# Display the plot
plt.show()
```

В этом коде мы используем различные параметры метода `plot()` для настройки графика. Мы меняем цвет линии на красный, ширину линии на 2, стиль линии на пунктирный (`--`), маркер на круг (`o`), размер маркера на 8 и цвет заливки маркера на желтый.
