# Ein weiteres inneres GridSpec erstellen

Wir werden nun ein weiteres inneres GridSpec erstellen. Diesmal werden wir die `subgridspec`-Methode verwenden, um ein 3 x 3-GridSpec zu erstellen, das ein Teilplot der zweiten Spalte des äußeren GridSpecs sein wird.

```python
gs01 = gs0[1].subgridspec(3, 3)
```
