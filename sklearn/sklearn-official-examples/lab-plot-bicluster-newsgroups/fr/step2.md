# Définir le normalisateur de nombres

Nous allons définir une fonction `number_normalizer()` pour mapper tous les jetons numériques à un emplacement réservé. Cela est utilisé pour la réduction de la dimensionalité.

```python
def number_normalizer(tokens):
    """Map all numeric tokens to a placeholder.

    For many applications, tokens that begin with a number are not directly
    useful, but the fact that such a token exists can be relevant.  By applying
    this form of dimensionality reduction, some methods may perform better.
    """
    return ("#NUMBER" if token[0].isdigit() else token for token in tokens)
```
