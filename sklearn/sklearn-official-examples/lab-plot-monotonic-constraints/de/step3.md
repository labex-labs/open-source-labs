# Ein Modell ohne Einschränkungen anpassen

Wir werden ein Modell auf den generierten Daten ohne jegliche Einschränkungen anpassen, um zu sehen, wie das Modell ohne jegliche Beschränkungen performt.

```python
gbdt_no_cst = HistGradientBoostingRegressor()
gbdt_no_cst.fit(X, y)
```
