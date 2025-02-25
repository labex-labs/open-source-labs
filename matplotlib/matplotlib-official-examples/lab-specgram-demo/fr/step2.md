# Générer un signal

Ensuite, nous allons générer un signal à tracer. Dans cet exemple, nous allons créer un signal qui est la somme de deux ondes sinusoïdales de fréquences différentes, et de bruit aléatoire.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

dt = 0.0005
t = np.arange(0.0, 20.0, dt)
s1 = np.sin(2 * np.pi * 100 * t)
s2 = 2 * np.sin(2 * np.pi * 400 * t)

# create a transient "chirp"
s2[t <= 10] = s2[12 <= t] = 0

# add some noise into the mix
nse = 0.01 * np.random.random(size=len(t))

x = s1 + s2 + nse  # le signal
```
