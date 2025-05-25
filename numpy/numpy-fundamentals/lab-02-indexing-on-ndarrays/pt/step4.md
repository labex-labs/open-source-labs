# Indexação Avançada

A indexação avançada é acionada quando o objeto de seleção `obj` é um objeto de sequência não-tupla, um ndarray (do tipo de dado inteiro ou booleano), ou uma tupla com pelo menos um objeto de sequência ou ndarray (do tipo de dado inteiro ou booleano). Existem dois tipos de indexação avançada: inteira e booleana.

## Indexação de Array Inteiro

A indexação de array inteiro permite a seleção de itens arbitrários no array com base em seu índice N-dimensional. Cada array inteiro representa um número de índices naquela dimensão.

```python
x = np.arange(10, 1, -1)
print(x[np.array([3, 3, 1, 8])])  # Output: [7, 7, 9, 2]
print(x[np.array([3, 3, -3, 8])])  # Output: [7, 7, 4, 2]
```

## Indexação de Array Booleano

A indexação de array booleano permite a seleção de elementos de array com base em uma condição booleana. O resultado é um novo array que contém apenas os elementos correspondentes aos valores `True` do array booleano.

```python
x = np.array([1., -1., -2., 3])
x[x < 0] += 20
print(x)  # Output: [ 1., 19., 18., 3.]
```
