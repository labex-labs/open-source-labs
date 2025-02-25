# Créez une fonction de formatage

Nous créons une fonction de formatage qui détermine l'étiquette de graduation à partir de la valeur à l'emplacement de la graduation. Si la valeur de la graduation est un entier dans la plage de `xs`, l'étiquette correspondante de la liste `labels` est renvoyée. Sinon, une chaîne de caractères vide est renvoyée.

```python
def format_fn(tick_val, tick_pos):
    if int(tick_val) in xs:
        return labels[int(tick_val)]
    else:
        return ''
```
