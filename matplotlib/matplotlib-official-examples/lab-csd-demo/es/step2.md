# Generar señales

Necesitamos generar dos señales. Estas señales contienen una parte coherente y una parte aleatoria. La parte coherente de ambas señales tiene una frecuencia de 10 Hz. La parte aleatoria de las señales se genera utilizando ruido blanco que se pasa a través de un filtro pasa-bajos para crear ruido coloreado.

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
