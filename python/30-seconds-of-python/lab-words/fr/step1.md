# Chaîne de caractères en mots

Écrivez une fonction `string_to_words(s: str, pattern: str = '[a-zA-Z-]+') -> List[str]` qui prend une chaîne de caractères `s` et une chaîne de caractères `pattern` optionnelle en arguments et renvoie une liste de mots dans la chaîne.

- La fonction devrait utiliser `re.findall()` avec le `pattern` fourni pour trouver toutes les sous-chaînes correspondantes.
- Si l'argument `pattern` n'est pas fourni, la fonction devrait utiliser l'expression rationnelle par défaut, qui correspond aux caractères alphanumériques et aux tirets.

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
