# Ajouter des caractères à une chaîne

## Problème

Écrivez une fonction `pad(s: str, length: int, char: str ='') -> str` qui ajoute des caractères spécifiés aux deux côtés d'une chaîne si elle est plus courte que la longueur spécifiée. La fonction doit prendre trois paramètres :

- `s` : une chaîne qui doit être ajoutée des caractères
- `length` : un entier qui spécifie la longueur totale de la chaîne ajoutée des caractères
- `char` : un caractère utilisé pour ajouter des caractères à la chaîne. La valeur par défaut est un caractère d'espace.

La fonction doit renvoyer la chaîne ajoutée des caractères.

## Exemple

```python
pad('cat', 8) #' cat   '
pad('42', 6, '0') # '004200'
pad('foobar', 3) # 'foobar'
```
