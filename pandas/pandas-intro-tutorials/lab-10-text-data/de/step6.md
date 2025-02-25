# Ersetze Werte in einer Spalte

Schließlich ersetzen wir die Werte in der Spalte `Sex`: ' männlich' durch 'M' und 'weiblich' durch 'F'. Dafür verwenden wir die Methode `replace()`.

```python
# Replace'male' with 'M' and 'female' with 'F' in the 'Sex' column
titanic["Sex_short"] = titanic["Sex"].replace({"male": "M", "female": "F"})
```
