# Создаем примерные данные

Теперь мы создадим некоторые примерные данные для построения с использованием `numpy`.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

x = np.arange(0.0, 5.0, 0.01)
y = np.sin(2 * np.pi * x) + 0.5 * np.random.randn(len(x))
```
