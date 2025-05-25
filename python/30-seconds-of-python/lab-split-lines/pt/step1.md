# Dividir em Linhas

Escreva uma função chamada `split_lines(s)` que recebe uma string multilinhas `s` como entrada e retorna uma lista de linhas individuais. Sua função deve dividir a string em cada quebra de linha (`\n`) e retornar uma lista das linhas resultantes.

```python
def split_lines(s):
  return s.split('\n')
```

```python
split_lines('This\nis a\nmultiline\nstring.\n')
# ['This', 'is a', 'multiline', 'string.' , '']
```
