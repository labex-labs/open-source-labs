# Gestion du cas du dictionnaire vide

Notre fonction actuelle a un problème : elle plantera si le dictionnaire d'entrée `d` est vide. Corrigeons cela. Modifiez `key_of_max.py` pour qu'il ressemble à ceci :

```python
def key_of_max(d):
  """
  Renvoie la clé associée à la valeur maximale dans le dictionnaire 'd'.

  Si plusieurs clés partagent la valeur maximale, l'une d'entre elles peut être renvoyée.
  """
  if not d:  # Check if the dictionary is empty
      return None
  return max(d, key=d.get)
```

Les lignes ajoutées font ce qui suit :

- **`if not d:`** : En Python, un dictionnaire vide est considéré comme "faux" (falsy). Cette instruction `if` vérifie si le dictionnaire `d` est vide.
- **`return None`** : Si le dictionnaire est vide, il n'y a pas de valeur maximale, donc nous renvoyons `None`. C'est une façon standard d'indiquer l'absence d'une valeur en Python. Cela empêche la fonction `max()` de lever une erreur.

Ceci est une étape cruciale dans l'écriture de code robuste : pensez toujours aux cas limites (edge cases)!
