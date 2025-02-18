# Генерация сигналов

Нам нужно сгенерировать два сигнала. Эти сигналы содержат когерентную часть и случайную часть. Когерентная часть обоих сигналов имеет частоту 10 Гц. Случайная часть сигналов генерируется с использованием белого шума, который пропускается через низкочастотный фильтр для создания цветного шума.

```python
dt = 0.01
t = np.arange(0, 30, dt)

# Fixing random state for reproducibility
np.random.seed(19680801)

nse1 = np.random.randn(len(t))                 # white noise 1
nse2 = np.random.randn(len(t))                 # white noise 2
r = np.exp(-t / 0.05)

cnse1 = np.convolve(nse1, r, mode='same') * dt   # colored noise 1
cnse2 = np.convolve(nse2, r, mode='same') * dt   # colored noise 2

# two signals with a coherent part and a random part
s1 = 0.01 * np.sin(2 * np.pi * 10 * t) + cnse1
s2 = 0.01 * np.sin(2 * np.pi * 10 * t) + cnse2
```
