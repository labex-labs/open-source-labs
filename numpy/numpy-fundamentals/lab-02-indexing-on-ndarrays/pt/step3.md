# Fatiamento (Slicing) e Passo (Striding)

O fatiamento básico em NumPy estende o conceito de fatiamento do Python para N dimensões. Ele permite que você selecione um intervalo de elementos ao longo de cada dimensão de um array.

## Fatiamento Básico

O fatiamento básico ocorre quando `obj` é um objeto slice (construído pela notação `start:stop:step` dentro de colchetes), um inteiro ou uma tupla de objetos slice e inteiros.

```python
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(x[1:7:2])  # Output: [1, 3, 5]
```

## Índices Negativos

Índices negativos podem ser usados para indexar a partir do final do array. Por exemplo, `-1` se refere ao último elemento, `-2` se refere ao penúltimo elemento e assim por diante.

```python
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(x[-2:10])  # Output: [8, 9]
print(x[-3:3:-1])  # Output: [7, 6, 5, 4]
```

## Valores Padrão para Fatiamento

Se o índice inicial não for especificado, ele assume o valor padrão de 0 para valores de passo positivos e `-n-1` para valores de passo negativos. Se o índice final não for especificado, ele assume o valor padrão de `n` para valores de passo positivos e `-n-1` para valores de passo negativos. Se o passo não for especificado, ele assume o valor padrão de 1.

```python
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(x[5:])  # Output: [5, 6, 7, 8, 9]
```
