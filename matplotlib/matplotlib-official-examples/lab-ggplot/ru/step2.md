# Создаем точечный график

Мы создадим точечный график с случайными точками данных.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# Create random data points
x, y = np.random.normal(size=(2, 200))

# Create a scatter plot
plt.plot(x, y, 'o')
plt.show()
```
