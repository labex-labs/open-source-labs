# String para Slug

Escreva uma função `slugify(s)` que recebe uma string `s` como argumento e retorna um slug. A função deve realizar as seguintes operações:

1. Converter a string para minúsculas e remover qualquer espaço em branco no início ou no fim.
2. Substituir todos os caracteres especiais (ou seja, qualquer caractere que não seja uma letra, dígito, espaço em branco, hífen ou sublinhado) por uma string vazia.
3. Substituir todos os espaços em branco, hífens e sublinhados por um único hífen.
4. Remover quaisquer hífens no início ou no fim.

```python
import re

def slugify(s):
  s = s.lower().strip()
  s = re.sub(r'[^\w\s-]', '', s)
  s = re.sub(r'[\s_-]+', '-', s)
  s = re.sub(r'^-+|-+$', '', s)
  return s
```

```python
slugify('Hello World!') # 'hello-world'
```
