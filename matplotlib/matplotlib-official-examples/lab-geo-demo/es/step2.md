# Crear una figura y subtramas

En este paso, crearemos una figura y cuatro subtramas para cada una de las proyecciones que crearemos. Utilizaremos el método `plt.subplots()` para crear una figura y subtramas.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, subplot_kw={'projection': 'aitoff'})
```
