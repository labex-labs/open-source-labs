# Ein Modell mit monotonen Einschränkungen anpassen

Wir werden nun ein weiteres Modell auf den gleichen Daten anpassen, jedoch mit monotonen Einschränkungen für die Merkmale. Wir werden eine monoton steigende Einschränkung für das erste Merkmal und eine monoton fallende Einschränkung für das zweite Merkmal auferlegen.

```python
gbdt_with_monotonic_cst = HistGradientBoostingRegressor(monotonic_cst=[1, -1])
gbdt_with_monotonic_cst.fit(X, y)
```
