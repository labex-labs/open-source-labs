# Den fehlenden Wert mit dem Skalar NA kennzeichnen verstehen

Schließlich werden wir das experimentelle `NA`-Skalar in pandas besprechen, das verwendet werden kann, um fehlende Werte zu kennzeichnen.

```python
s = pd.Series([1, 2, None], dtype="Int64")
s
```
