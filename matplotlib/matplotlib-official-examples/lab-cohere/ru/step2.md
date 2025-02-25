# Генерация сигналов

Далее мы сгенерируем два сигнала, состоящие из когерентной части с частотой 10 Гц и случайной части. Также добавим белый шум к сигналам.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

dt = 0.01
t = np.arange(0, 30, dt)
nse1 = np.random.randn(len(t))                 # white noise 1
nse2 = np.random.randn(len(t))                 # white noise 2

s1 = np.sin(2 * np.pi * 10 * t) + nse1
s2 = np.sin(2 * np.pi * 10 * t) + nse2
```
