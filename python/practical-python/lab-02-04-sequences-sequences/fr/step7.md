# Instruction `continue`

Pour sauter un élément et passer au suivant, utilisez l'instruction `continue`.

```python
for line in lines:
    if line == '\n':    # Sauter les lignes vides
        continue
    # Plus d'instructions
 ...
```

Cela est utile lorsque l'élément actuel n'est pas d'intérêt ou doit être ignoré dans le traitement.
