# Indexação do Iterador Flat

O atributo `x.flat` retorna um iterador que pode ser usado para iterar sobre todo o array no estilo C-contiguous. Este iterador também pode ser indexado usando slicing básico ou indexação avançada.

```python
x = np.arange(10)
iterator = x.flat
print(iterator[1:5])  # Output: [1, 2, 3, 4]
```
