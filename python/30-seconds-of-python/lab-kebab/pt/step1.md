# String em Kebab Case

Escreva uma função Python chamada `to_kebab_case(s)` que recebe uma string `s` como entrada e retorna a versão em _kebab case_ da string. A função deve realizar as seguintes etapas:

1.  Substituir qualquer `-` ou `_` por um espaço, usando a expressão regular (regexp) `r"(_|-)+"`.
2.  Encontrar todas as palavras na string, usando `str.lower()` para colocá-las em minúsculas.
3.  Combinar todas as palavras usando `-` como separador.

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
