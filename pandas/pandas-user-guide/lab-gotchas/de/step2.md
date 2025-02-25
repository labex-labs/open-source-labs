# Das Verwenden von if/Wahrheitsaussagen mit Pandas

Aufgrund der Mehrdeutigkeit unterstützt Pandas die direkte Verwendung von if/Wahrheitsaussagen nicht. Verwenden Sie stattdessen Methoden wie `.any()`, `.all()` oder `.empty()`.

```python
# Überprüfen, ob in der Series mindestens ein Wert True ist
if pd.Series([False, True, False]).any():
    print("Mindestens ein True-Wert in der Series")
```
