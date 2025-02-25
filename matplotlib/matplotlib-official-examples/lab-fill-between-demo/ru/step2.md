# Доверительные интервалы

Одно из распространенных применений функции `fill_between` - это показ доверительных интервалов. Функция `fill_between` использует цвета из цикла цветов в качестве цвета заливки. Поэтому часто хорошей практикой является осветление цвета, сделав область полупрозрачной с использованием параметра _alpha_.

```python
N = 21
x = np.linspace(0, 10, 11)
y = [3.9, 4.4, 10.8, 10.3, 11.2, 13.1, 14.1,  9.9, 13.9, 15.1, 12.5]

# fit a linear curve and estimate its y-values and their error.
a, b = np.polyfit(x, y, deg=1)
y_est = a * x + b
y_err = x.std() * np.sqrt(1/len(x) +
                          (x - x.mean())**2 / np.sum((x - x.mean())**2))

fig, ax = plt.subplots()
ax.plot(x, y_est, '-')
ax.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.2)
ax.plot(x, y, 'o', color='tab:brown')
```
