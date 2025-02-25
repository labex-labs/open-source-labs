# Cargar la imagen

Usaremos el método `get_sample_data` de `cbook` para cargar una imagen de muestra. Este método devuelve un objeto similar a un archivo, que podemos pasar a `imshow` para mostrar la imagen.

```python
with cbook.get_sample_data('grace_hopper.jpg') as image_file:
    image = plt.imread(image_file)
```
