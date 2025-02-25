# Построение графика

Теперь мы построим график, используя `np.linspace` и `np.sin`.

```python
x = np.linspace(-0.5, 1., 100)
ax.plot(x, np.sin(x*np.pi))
```
