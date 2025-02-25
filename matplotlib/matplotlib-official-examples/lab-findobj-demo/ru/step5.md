# Создание различных типов графиков

Matplotlib поддерживает широкий спектр типов графиков, включая линейные графики, точечные графики, столбчатые графики и многие другие. Вот пример кода, который создает точечный график:

```python
import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

# Create a scatter plot
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')

# Display the plot
plt.show()
```

В этом коде мы используем метод `scatter()`, чтобы создать точечный график. Мы генерируем некоторые случайные данные с использованием библиотеки NumPy и передаем их методу `scatter()`. Мы также используем параметр `c`, чтобы указать цвета точек данных, параметр `s`, чтобы указать размеры точек данных, и параметр `alpha`, чтобы указать прозрачность точек данных.
