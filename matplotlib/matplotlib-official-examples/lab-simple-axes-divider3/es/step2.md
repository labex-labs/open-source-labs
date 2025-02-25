# Configurar la figura y los ejes

Crearemos un objeto de figura y configuraremos cuatro objetos de ejes utilizando el método `fig.add_axes`.

```python
fig = plt.figure(figsize=(5.5, 4))
rect = (0.1, 0.1, 0.8, 0.8)
ax = [fig.add_axes(rect, label="%d" % i) for i in range(4)]
```
