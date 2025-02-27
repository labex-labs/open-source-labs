# Generar datos

Generaremos un conjunto de datos artificial donde el valor objetivo está correlacionado positivamente con la primera característica y negativamente con la segunda característica. También agregaremos algo de ruido aleatorio para que los datos sean más realistas.

```python
rng = np.random.RandomState(0)

n_samples = 1000
f_0 = rng.rand(n_samples)
f_1 = rng.rand(n_samples)
X = np.c_[f_0, f_1]
noise = rng.normal(loc=0.0, scale=0.01, size=n_samples)

y = 5 * f_0 + np.sin(10 * np.pi * f_0) - 5 * f_1 - np.cos(10 * np.pi * f_1) + noise
```
