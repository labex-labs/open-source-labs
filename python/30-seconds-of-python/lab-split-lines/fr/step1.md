# Diviser en lignes

Écrivez une fonction appelée `split_lines(s)` qui prend une chaîne multiligne `s` en entrée et renvoie une liste des lignes individuelles. Votre fonction devrait diviser la chaîne à chaque saut de ligne (`\n`) et renvoyer une liste des lignes résultantes.

```python
def split_lines(s):
  return s.split('\n')
```

```python
split_lines('This\nis a\nmultiline\nstring.\n')
# ['This', 'is a','multiline','string.', '']
```
