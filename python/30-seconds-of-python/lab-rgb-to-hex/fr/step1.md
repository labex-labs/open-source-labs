# Conversion RGB en hexadécimal

Écrivez une fonction `rgb_to_hex(r, g, b)` qui prend trois entiers représentant les valeurs des composantes rouge, verte et bleue d'une couleur, et renvoie une chaîne de caractères représentant le code couleur hexadécimal. La chaîne de caractères de sortie doit être au format `RRGGBB`, où `RR`, `GG` et `BB` sont des valeurs hexadécimales sur deux chiffres représentant respectivement les composantes rouge, verte et bleue.

Par exemple, si les valeurs d'entrée sont `255`, `165` et `1`, la sortie devrait être la chaîne de caractères `'FFA501'`.

```python
def rgb_to_hex(r, g, b):
  return ('{:02X}' * 3).format(r, g, b)
```

```python
rgb_to_hex(255, 165, 1) # 'FFA501'
```
