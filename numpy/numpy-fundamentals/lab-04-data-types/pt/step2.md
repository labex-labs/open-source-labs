# Trabalhando com Tipos de Dados

Os tipos de dados NumPy são representados como objetos `dtype` (data-type). Depois de importar NumPy usando `import numpy as np`, você pode acessar os tipos de dados usando `np.bool_`, `np.float32`, etc.

Você pode usar tipos de dados como funções para converter números Python em escalares de array, sequências Python de números em arrays desse tipo, ou como argumentos para a palavra-chave `dtype` em muitas funções ou métodos NumPy. Aqui estão alguns exemplos:

```python
x = np.float32(1.0)
# x is now a float32 array scalar with value 1.0

y = np.int_([1,2,4])
# y is now an int array with values [1, 2, 4]

z = np.arange(3, dtype=np.uint8)
# z is now a uint8 array with values [0, 1, 2]
```

Você também pode se referir aos tipos de array usando códigos de caracteres, embora seja recomendado usar objetos `dtype` em vez disso. Por exemplo:

```python
np.array([1, 2, 3], dtype='f')
# returns an array with values [1., 2., 3.] and dtype float32
```

Para converter o tipo de um array, você pode usar o método `.astype()` ou o próprio tipo como uma função. Por exemplo:

```python
z.astype(float)
# returns the array z with dtype float64

np.int8(z)
# returns the array z with dtype int8
```
