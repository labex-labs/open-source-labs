# Inteiro para Algarismo Romano

Escreva uma função `to_roman_numeral(num)` que recebe um inteiro `num` entre 1 e 3999 (inclusive) e retorna sua representação em algarismos romanos como uma string.

Para converter um inteiro para sua representação em algarismos romanos, você pode usar uma lista de pesquisa contendo tuplas na forma de (valor romano, inteiro). Em seguida, você pode usar um loop `for` para iterar sobre os valores na lista de pesquisa e usar `divmod()` para atualizar `num` com o resto, adicionando a representação em algarismos romanos ao resultado.

Sua função deve retornar a representação em algarismos romanos do inteiro de entrada.

```python
def to_roman_numeral(num):
  lookup = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I'),
  ]
  res = ''
  for (n, roman) in lookup:
    (d, num) = divmod(num, n)
    res += roman * d
  return res
```

```python
to_roman_numeral(3) # 'III'
to_roman_numeral(11) # 'XI'
to_roman_numeral(1998) # 'MCMXCVIII'
```
