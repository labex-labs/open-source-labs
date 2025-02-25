# Création du signal

Nous allons créer un signal à l'aide de NumPy. Nous allons créer un tableau `xdata` à l'aide de la fonction `linspace` avec `start = 16`, `stop = 365` et `num=(365 - 16)*4`. Nous allons créer un tableau `ydata` à l'aide des fonctions `sin` et `cos`.

```python
xdata = np.linspace(16, 365, (365-16)*4)
ydata = np.sin(2*np.pi*xdata/153) + np.cos(2*np.pi*xdata/127)
```
