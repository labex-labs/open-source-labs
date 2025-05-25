# String para Palavras (String to Words)

Escreva uma função `string_to_words(s: str, pattern: str = '[a-zA-Z-]+') -> List[str]` que recebe uma string `s` e uma string `pattern` opcional como argumentos e retorna uma lista de palavras na string.

- A função deve usar `re.findall()` com o `pattern` fornecido para encontrar todas as substrings correspondentes.
- Se o argumento `pattern` não for fornecido, a função deve usar a expressão regular (regexp) padrão, que corresponde a caracteres alfanuméricos e hífens.

```python
import re

def words(s, pattern = '[a-zA-Z-]+'):
  return re.findall(pattern, s)
```

```python
words('I love Python!!') # ['I', 'love', 'Python']
words('python, javaScript & coffee') # ['python', 'javaScript', 'coffee']
words('build -q --out one-item', r'\b[a-zA-Z-]+\b')
# ['build', 'q', 'out', 'one-item']
```
