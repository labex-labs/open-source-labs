# Kleene-Logische Operationen

Pandas implementiert die Kleene-Logik (Drei-Wert-Logik) für logische Operationen wie `&` (und), `|` (oder) und `^` (exklusives Oder). Dies unterscheidet sich von der Verhalten von `np.nan` in logischen Operationen.

```python
# Demonstration des Unterschieds in den 'oder'-Operationen zwischen np.nan und NA
pd.Series([True, False, np.nan], dtype="object") | True # np.nan verhält sich anders
pd.Series([True, False, pd.NA], dtype="boolean") | True # NA folgt der Kleene-Logik

# Demonstration des Unterschieds in den 'und'-Operationen zwischen np.nan und NA
pd.Series([True, False, np.nan], dtype="object") & True # np.nan verhält sich anders
pd.Series([True, False, pd.NA], dtype="boolean") & True # NA folgt der Kleene-Logik
```
