# String wiederholen

Schreiben Sie eine Funktion namens `repeat_string`, die zwei Parameter akzeptiert: einen String `s` und eine Ganzzahl `n`. Die Funktion sollte einen neuen String zurückgeben, der `s` `n` Mal wiederholt enthält.

Beispielsweise sollte die Funktion, wenn `s` `"hello"` ist und `n` `3` ist, `"hellohellohello"` zurückgeben. Wenn `s` `"abc"` ist und `n` `5` ist, sollte die Funktion `"abcabcabcabcabc"` zurückgeben.

```python
def n_times_string(s, n):
  return (s * n)
```

```python
n_times_string('py', 4) #'pypypypy'
```
