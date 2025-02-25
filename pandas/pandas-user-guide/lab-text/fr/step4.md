# Vérifier des chaînes de caractères

Vous pouvez vérifier si des éléments contiennent ou correspondent à un motif en utilisant respectivement les méthodes `contains` et `match`.

```python
# vérifier si chaque chaîne contient le motif "a"
s.str.contains("a", na=False)

# vérifier si chaque chaîne correspond au motif "a"
s.str.match("a", na=False)
```
