# Fehler und Ausnahmen

Funktionen melden Fehler als Ausnahmen. Eine Ausnahme bewirkt, dass eine Funktion abgebrochen wird und kann, wenn nicht behandelt, dazu führen, dass Ihr gesamtes Programm stoppt.

Versuchen Sie das in Ihrem Python-REPL.

```python
>>> int('N/A')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'N/A'
>>>
```

Zwecks Debugging beschreibt die Nachricht, was passiert ist, wo der Fehler aufgetreten ist und einen Stapelverlauf, der die anderen Funktionsaufrufe zeigt, die zum Fehler geführt haben.
