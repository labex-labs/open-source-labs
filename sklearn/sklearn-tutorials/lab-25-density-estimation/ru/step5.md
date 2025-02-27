# Визуализируем оценку плотности

Наконец, мы можем визуализировать оценку плотности с использованием гистограммы и оцененной функции плотности. Мы можем построить гистограмму исходных данных, а также оцененную функцию плотности.

```python
import matplotlib.pyplot as plt

bins = np.linspace(-5, 5, 50)
plt.hist(X, bins=bins, density=True, alpha=0.5, label='Histogram')
plt.plot(X, np.exp(scores), color='red', label='Kernel Density Estimate')
plt.legend()
plt.show()
```
