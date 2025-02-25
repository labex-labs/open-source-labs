# Définir la fonction explode

Ensuite, nous définissons une fonction appelée `explode` qui sera utilisée pour agrandir l'image en voxels du logo de NumPy. Cette fonction prend un tableau NumPy en entrée et renvoie un nouveau tableau NumPy qui est deux fois plus grand que le tableau d'entrée.

```python
def explode(data):
    size = np.array(data.shape)*2
    data_e = np.zeros(size - 1, dtype=data.dtype)
    data_e[::2, ::2, ::2] = data
    return data_e
```
