# Übung 1.18: Reguläre Ausdrücke

Eine Einschränkung der grundlegenden String-Operationen ist, dass sie keine Art von fortgeschrittenen Mustervergleichen unterstützen. Dazu müssen Sie sich auf das `re`-Modul von Python und reguläre Ausdrücke verlassen. Das Thema der Behandlung regulärer Ausdrücke ist ein umfangreiches Thema, aber hier ist ein kurzes Beispiel:

```python
>>> text = 'Today is 3/27/2018. Tomorrow is 3/28/2018.'
>>> # Findet alle Vorkommen eines Datums
>>> import re
>>> re.findall(r'\d+/\d+/\d+', text)
['3/27/2018', '3/28/2018']
>>> # Ersetzt alle Vorkommen eines Datums durch Ersatztext
>>> re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
'Today is 2018-3-27. Tomorrow is 2018-3-28.'
>>>
```

Weitere Informationen über das `re`-Modul finden Sie in der offiziellen Dokumentation unter [https://docs.python.org/library/re.html](https://docs.python.org/3/library/re.html).
