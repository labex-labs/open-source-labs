# Генерируем данные

Мы генерируем некоторые образцовые данные для построения, используя функцию `mgrid` из `numpy`.

```python
# setup some generic data
N = 37
x, y = np.mgrid[:N, :N]
Z = (np.cos(x*0.2) + np.sin(y*0.3))
```
