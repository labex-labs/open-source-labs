# Crear una figura y ejes

Crearemos una figura y un objeto de ejes utilizando `plt.subplots()`. La función `imshow()` se utiliza para mostrar los datos aleatorios como una imagen.

```python
fig, ax = plt.subplots()

image = np.random.uniform(size=(10, 10))
ax.imshow(image, cmap=plt.cm.gray)
ax.set_title('espinas caídas')
```
