# Definir a função explode

Em seguida, definimos uma função chamada `explode` que será usada para aumentar a escala da imagem de voxel do logotipo do NumPy. Esta função recebe um array NumPy como entrada e retorna um novo array NumPy que é o dobro do tamanho do array de entrada.

```python
def explode(data):
    size = np.array(data.shape)*2
    data_e = np.zeros(size - 1, dtype=data.dtype)
    data_e[::2, ::2, ::2] = data
    return data_e
```
