# Remplissage de nombre

## Problème

Écrivez une fonction `pad_number(n, l)` qui prend un nombre `n` et une longueur `l` et renvoie une chaîne de caractères représentant le nombre rempli. La fonction devrait remplir le nombre de zéros initiaux pour le rendre de longueur `l` chiffres. Si le nombre est déjà de longueur `l` chiffres, la fonction devrait renvoyer le nombre sous forme de chaîne de caractères.

Pour remplir le nombre, vous pouvez utiliser la méthode `str.zfill()`. Cette méthode prend une longueur et remplit la chaîne de caractères de zéros initiaux jusqu'à ce qu'elle atteigne cette longueur. Par exemple, `"7".zfill(6)` renverrait `"000007"`.

## Exemple

```python
pad_number(1234, 6) # '001234'
pad_number(7, 6) # '000007'
pad_number(123456789, 9) # '123456789'
```
