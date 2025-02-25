# Fehlende Daten einfügen

Hier sehen wir, wie man fehlende Werte in unsere Daten einfügt.

```python
# Fehlende Werte einfügen
s = pd.Series([1., 2., 3.])
s.loc[0] = None
```
