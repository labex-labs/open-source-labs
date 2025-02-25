# Extraire le tampon du render dans un tableau numpy

La deuxième option pour enregistrer le tracé est d'extraire le tampon du render dans un tableau numpy. Cela nous permet d'utiliser Matplotlib dans un script cgi sans avoir besoin d'écrire une figure sur le disque. Dans cet exemple, nous allons extraire le tampon du render et le convertir en un tableau numpy.

```python
canvas.draw()
rgba = np.asarray(canvas.buffer_rgba())
```
