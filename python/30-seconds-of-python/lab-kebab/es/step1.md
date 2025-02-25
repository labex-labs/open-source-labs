# Cadena en formato kebab case

Escribe una función de Python llamada `to_kebab_case(s)` que tome una cadena `s` como entrada y devuelva la versión en formato kebab case de la cadena. La función debe realizar los siguientes pasos:

1. Reemplazar cualquier `-` o `_` con un espacio, utilizando la expresión regular `r"(_|-)+"`.
2. Encontrar todas las palabras en la cadena y convertirlas a minúsculas con `str.lower()`.
3. Combinar todas las palabras utilizando `-` como separador.

```python
from re import sub

def kebab(s):
  return '-'.join(
    sub(r"(\s|_|-)+"," ",
    sub(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+",
    lambda mo: ' ' + mo.group(0).lower(), s)).split())
```

```python
kebab('camelCase') # 'camel-case'
kebab('some text') # 'some-text'
kebab('some-mixed_string With spaces_underscores-and-hyphens')
# 'some-mixed-string-with-spaces-underscores-and-hyphens'
kebab('AllThe-small Things') # 'all-the-small-things'
```
