# Utiliser des instructions if/condition de vérité avec Pandas

Pandas ne prend pas en charge l'utilisation directe d'instructions if/condition de vérité en raison de l'ambiguité. Utilisez plutôt des méthodes telles que `.any()`, `.all()` ou `.empty()`.

```python
# Vérifier si une valeur dans la Séries est True
if pd.Series([False, True, False]).any():
    print("Au moins une valeur True dans la Séries")
```
