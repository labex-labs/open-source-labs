# Capitalizar String

Escreva uma função Python chamada `capitalize_string(s, lower_rest=False)` que recebe uma string como argumento e retorna uma nova string com a primeira letra capitalizada. A função deve ter um parâmetro opcional `lower_rest` que, se definido como `True`, converte o restante da string para minúsculas.

```python
def capitalize(s, lower_rest = False):
  return ''.join([s[:1].upper(), (s[1:].lower() if lower_rest else s[1:])])
```

```python
capitalize('fooBar') # 'FooBar'
capitalize('fooBar', True) # 'Foobar'
```
