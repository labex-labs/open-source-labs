# Répéter une chaîne de caractères

Écrivez une fonction appelée `repeat_string` qui prend deux paramètres : une chaîne de caractères `s` et un entier `n`. La fonction devrait renvoyer une nouvelle chaîne de caractères qui contient `s` répétée `n` fois.

Par exemple, si `s` est `"hello"` et `n` est `3`, la fonction devrait renvoyer `"hellohellohello"`. Si `s` est `"abc"` et `n` est `5`, la fonction devrait renvoyer `"abcabcabcabcabc"`.

```python
def n_times_string(s, n):
  return (s * n)
```

```python
n_times_string('py', 4) #'pypypypy'
```
