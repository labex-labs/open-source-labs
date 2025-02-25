# Rohstrings

Rohstrings sind String-Literale mit einem nicht interpretierten Backslash. Sie werden durch Präfixieren der anfänglichen Anführungszeichen mit einem kleinen "r" angegeben.

```python
>>> rs = r'c:\newdata\test' # Roh (nicht interpretierten Backslash)
>>> rs
'c:\\newdata\\test'
```

Der String ist der literale Text, der darin eingeschlossen ist, genau wie er eingegeben wurde. Dies ist nützlich in Situationen, in denen der Backslash besondere Bedeutung hat. Beispiel: Dateiname, reguläre Ausdrücke usw.
