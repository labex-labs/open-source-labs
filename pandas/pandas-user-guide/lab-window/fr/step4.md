# Effectuer une opération de fenêtre pondérée exponentiellement

Effectuez une opération de fenêtre pondérée exponentiellement puis calculez la moyenne pour chaque fenêtre.

```python
# Effectuez une opération de fenêtre pondérée exponentiellement et calculez la moyenne pour chaque fenêtre
s.ewm(span=3).mean()
```
