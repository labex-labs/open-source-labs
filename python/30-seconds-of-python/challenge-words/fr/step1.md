# Défi : Conversion d'une chaîne de caractères en mots

## Problème

Écrivez une fonction `string_to_words(s: str, pattern: str = '[a-zA-Z-]+') -> List[str]` qui prend une chaîne de caractères `s` et une chaîne de caractères `pattern` optionnelle en arguments et renvoie une liste de mots dans la chaîne.

- La fonction devrait utiliser `re.findall()` avec le `pattern` fourni pour trouver toutes les sous-chaînes correspondantes.
- Si l'argument `pattern` n'est pas fourni, la fonction devrait utiliser l'expression rationnelle par défaut, qui correspond aux caractères alphanumériques et aux tirets.

## Exemple

```python
string_to_words('I love Python!!') # ['I', 'love', 'Python']
string_to_words('python, javaScript & coffee') # ['python', 'javaScript', 'coffee']
string_to_words('build -q --out one-item', r'\b[a-zA-Z-]+\b') # ['build', 'q', 'out', 'one-item']
```
