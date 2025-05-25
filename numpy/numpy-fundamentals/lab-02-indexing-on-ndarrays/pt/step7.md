# Atribuindo Valores a Arrays Indexados

Você pode atribuir valores a elementos específicos ou subconjuntos de elementos em um array usando indexação. O valor que está sendo atribuído deve ter uma forma (shape) consistente com o array indexado.

```python
x = np.arange(10)
x[2:7] = 1
print(x)  # Output: [0, 1, 1, 1, 1, 1, 7, 8, 9]

x = np.arange(10)
x[2:7] = np.arange(5)
print(x)  # Output: [0, 1, 0, 1, 2, 3, 7, 8, 9]
```
