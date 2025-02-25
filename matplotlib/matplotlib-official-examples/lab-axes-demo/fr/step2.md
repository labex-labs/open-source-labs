# Générer des données

Dans cette étape, nous générons quelques données pour les utiliser dans le graphique. Nous allons créer un bruit gaussien coloré à l'aide de la fonction `convolve` de NumPy et le tracer à l'aide de Matplotlib.

```python
np.random.seed(19680801)
dt = 0.001
t = np.arange(0.0, 10.0, dt)
r = np.exp(-t[:1000] / 0.05)
x = np.random.randn(len(t))
s = np.convolve(x, r)[:len(x)] * dt

fig, main_ax = plt.subplots()
main_ax.plot(t, s)
```
