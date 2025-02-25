# Настраиваем гистограмму

Мы можем настроить гистограмму, изменив цвет, прозрачность и цвет границ столбцов с использованием параметров `color`, `alpha` и `edgecolor`.

```python
plt.hist(x, n_bins, color='green', alpha=0.5, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')
plt.show()
```
