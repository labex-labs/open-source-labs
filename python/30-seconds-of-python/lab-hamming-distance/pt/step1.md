# Distância de Hamming

Escreva uma função `hamming_distance(a, b)` que recebe dois inteiros como argumentos e retorna a distância de Hamming entre eles. A função deve realizar os seguintes passos:

1.  Use o operador XOR (`^`) para encontrar a diferença de bits entre os dois números.
2.  Use `bin()` para converter o resultado em uma string binária.
3.  Converta a string em uma lista e use `count()` da classe `str` para contar e retornar o número de `1`s nela.

```python
def hamming_distance(a, b):
  return bin(a ^ b).count('1')
```

```python
hamming_distance(2, 3) # 1
```
