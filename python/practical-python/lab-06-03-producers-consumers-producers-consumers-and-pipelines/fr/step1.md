# Problèmes producteur-consommateur

Les générateurs sont étroitement liés à diverses formes de problèmes _producteur-consommateur_.

```python
# Producteur
def follow(f):
  ...
    while True:
      ...
        yield line        # Génère la valeur dans `line` ci-dessous
      ...

# Consommateur
for line in follow(f):    # Consomme la valeur provenant de `yield` ci-dessus
  ...
```

`yield` génère des valeurs que `for` consomme.
