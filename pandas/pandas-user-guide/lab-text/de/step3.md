# Teilstrings extrahieren

Sie können Teilstrings mit regulären Ausdrücken extrahieren. Die `extract`-Methode akzeptiert einen regulären Ausdruck mit mindestens einer Capturing-Gruppe.

```python
# extrahiere die erste Ziffer aus jedem String
s = pd.Series(["a1", "b2", "c3"], dtype="string")
s.str.extract(r"(\d)", expand=False)
```
