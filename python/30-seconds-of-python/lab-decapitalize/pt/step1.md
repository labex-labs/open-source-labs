# Descapitalizar String

Escreva uma função `decapitalize(s, upper_rest = False)` que recebe uma string `s` e retorna uma nova string com a primeira letra descapitalizada. A função também deve ter um parâmetro opcional `upper_rest` que, quando definido como `True`, converterá o restante da string para maiúsculas.

```python
def decapitalize(s, upper_rest = False):
  return ''.join([s[:1].lower(), (s[1:].upper() if upper_rest else s[1:])])
```

```python
decapitalize('FooBar') # 'fooBar'
decapitalize('FooBar', True) # 'fOOBAR'
```
