# Preencher String (Pad String)

Escreva uma função `pad(s: str, length: int, char: str = ' ') -> str` que preenche uma string em ambos os lados com o caractere especificado, se ela for menor que o comprimento especificado. A função deve receber três parâmetros:

- `s`: uma string que precisa ser preenchida
- `length`: um inteiro que especifica o comprimento total da string preenchida
- `char`: um caractere que é usado para preencher a string. O valor padrão é um caractere de espaço em branco.

A função deve retornar a string preenchida.

```python
from math import floor

def pad(s, length, char = ' '):
  return s.rjust(floor((len(s) + length)/2), char).ljust(length, char)
```

```python
pad('cat', 8) # '  cat   '
pad('42', 6, '0') # '004200'
pad('foobar', 3) # 'foobar'
```
