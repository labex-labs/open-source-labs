# Настройка библиотек и создание примерных данных

В этом первом шаге мы импортируем необходимые библиотеки и создадим примерные финансовые данные для нашего графика. Нам нужно импортировать как Matplotlib для визуализации, так и NumPy для генерации данных.

В первой ячейке вашего блокнота введите и запустите следующий код для импорта требуемых библиотек:

```python
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Display plots inline in the notebook
%matplotlib inline

print("Libraries imported successfully!")
```

После запуска кода (нажмите Shift+Enter) вы должны увидеть следующий вывод:

```
Libraries imported successfully!
```

![libraries-imported](../assets/screenshot-20250306-BN9E08ez@2x.png)

Теперь давайте создадим некоторые примерные финансовые данные для визуализации. Финансовые данные часто представляют значения в течение времени, поэтому мы создадим простой набор данных, который может представлять ежедневную выручку за определенный период.

В новой ячейке добавьте и запустите следующий код:

```python
# Set a random seed for reproducibility
np.random.seed(42)

# Generate financial data: 30 days of revenue data
days = np.arange(1, 31)
daily_revenue = np.random.uniform(low=1000, high=5000, size=30)

print("Sample of daily revenue data (first 5 days):")
for i in range(5):
    print(f"Day {days[i]}: ${daily_revenue[i]:.2f}")
```

После запуска этого кода вы увидите данные о выручке за первые 5 дней нашего примера:

```
Sample of daily revenue data (first 5 days):
Day 1: $3745.40
Day 2: $3992.60
Day 3: $2827.45
Day 4: $4137.54
Day 5: $1579.63
```

Эти примерные данные представляют ежедневные значения выручки от $1000 до $5000 за период в 30 дней. Мы будем использовать эти данные для создания нашего графика на следующем шаге.
