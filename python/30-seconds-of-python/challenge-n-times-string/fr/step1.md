# Répéter une chaîne de caractères

## Problème

Écrire une fonction appelée `repeat_string` qui prend deux paramètres : une chaîne de caractères `s` et un entier `n`. La fonction devrait renvoyer une nouvelle chaîne de caractères qui contient `s` répétée `n` fois.

Par exemple, si `s` est `"hello"` et `n` est `3`, la fonction devrait renvoyer `"hellohellohello"`. Si `s` est `"abc"` et `n` est `5`, la fonction devrait renvoyer `"abcabcabcabcabc"`.

## Exemple

```python
assert repeat_string("hello", 3) == "hellohellohello"
assert repeat_string("abc", 5) == "abcabcabcabcabc"
assert repeat_string("123", 2) == "123123"
```
