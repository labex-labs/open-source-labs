# Générer un signal

Nous allons générer un signal et le visualiser à l'aide de Matplotlib.

```python
resolution = 1024
subsampling = 3  # facteur de sous-échantillonnage
width = 100
n_components = resolution // subsampling

# Générer un signal
y = np.linspace(0, resolution - 1, resolution)
first_quarter = y < resolution / 4
y[first_quarter] = 3.0
y[np.logical_not(first_quarter)] = -1.0

# Visualiser le signal
plt.figure()
plt.plot(y)
plt.title("Signal original")
plt.show()
```
