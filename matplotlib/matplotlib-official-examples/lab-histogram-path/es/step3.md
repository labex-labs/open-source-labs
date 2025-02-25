# Generar los datos del histograma

Ahora que tenemos nuestros datos aleatorios, podemos generar un histograma usando numpy. Usaremos 50 intervalos para crear nuestro histograma. Agrega el siguiente código:

```python
n, bins = np.histogram(data, 50)
```
