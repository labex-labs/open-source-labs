# Definir la función explode

A continuación, definimos una función llamada `explode` que se utilizará para aumentar en tamaño la imagen de voxeles del logotipo de NumPy. Esta función toma una matriz de NumPy como entrada y devuelve una nueva matriz de NumPy que es el doble del tamaño de la matriz de entrada.

```python
def explode(data):
    size = np.array(data.shape)*2
    data_e = np.zeros(size - 1, dtype=data.dtype)
    data_e[::2, ::2, ::2] = data
    return data_e
```
