# Generar una señal

Generaremos una señal y la visualizaremos utilizando Matplotlib.

```python
resolution = 1024
subsampling = 3  # factor de submuestreo
width = 100
n_components = resolution // subsampling

# Generar una señal
y = np.linspace(0, resolution - 1, resolution)
first_quarter = y < resolution / 4
y[first_quarter] = 3.0
y[np.logical_not(first_quarter)] = -1.0

# Visualizar la señal
plt.figure()
plt.plot(y)
plt.title("Señal original")
plt.show()
```
