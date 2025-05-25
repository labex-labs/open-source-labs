# Indexação Básica

Arrays NumPy podem ser indexados usando a sintaxe Python padrão `x[obj]`, onde `x` é o array e `obj` é a seleção. Existem diferentes tipos de indexação disponíveis, dependendo do tipo de `obj`.

## Indexação de Elemento Único

A indexação de elemento único funciona exatamente como a indexação para outras sequências Python padrão. É baseada em 0 e aceita índices negativos para indexar a partir do final do array.

```python
x = np.arange(10)
print(x[2])  # Output: 2
print(x[-2])  # Output: 8
```

## Indexação Multidimensional

Arrays podem ter múltiplas dimensões, e a indexação funciona da mesma forma para cada dimensão. Você pode acessar elementos em um array multidimensional separando o índice de cada dimensão com uma vírgula.

```python
x = np.arange(10).reshape(2, 5)
print(x[1, 3])  # Output: 8
print(x[1, -1])  # Output: 9
```

## Indexação de Array Subdimensional

Se você indexar um array multidimensional com menos índices do que dimensões, você obtém um array subdimensional. Cada índice especificado seleciona o array correspondente ao restante das dimensões selecionadas.

```python
x = np.arange(10).reshape(2, 5)
print(x[0])  # Output: [0, 1, 2, 3, 4]
```
