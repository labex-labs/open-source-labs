# String wiederholen

## Problem

Schreiben Sie eine Funktion namens `repeat_string`, die zwei Parameter akzeptiert: einen String `s` und eine Ganzzahl `n`. Die Funktion sollte einen neuen String zurückgeben, der `s` `n` Mal wiederholt enthält.

Beispielsweise sollte die Funktion, wenn `s` `"hello"` ist und `n` `3` ist, `"hellohellohello"` zurückgeben. Wenn `s` `"abc"` ist und `n` `5` ist, sollte die Funktion `"abcabcabcabcabc"` zurückgeben.

## Beispiel

```python
assert repeat_string("hello", 3) == "hellohellohello"
assert repeat_string("abc", 5) == "abcabcabcabcabc"
assert repeat_string("123", 2) == "123123"
```
