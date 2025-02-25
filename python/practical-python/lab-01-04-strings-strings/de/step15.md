# Übung 1.16: String-Methoden

Am Python interaktiven Prompt können Sie mit einigen der String-Methoden experimentieren.

```python
>>> symbols.lower()
?
>>> symbols
?
>>>
```

Denken Sie daran, dass Strings immer schreibgeschützt sind. Wenn Sie das Ergebnis einer Operation speichern möchten, müssen Sie es in eine Variable ablegen:

```python
>>> lowersyms = symbols.lower()
>>>
```

Versuchen Sie einige weitere Operationen:

```python
>>> symbols.find('MSFT')
?
>>> symbols[13:17]
?
>>> symbols = symbols.replace('SCO','DOA')
>>> symbols
?
>>> name = '   IBM   \n'
>>> name = name.strip()    # Entfernt die umgebenden Leerzeichen
>>> name
?
>>>
```
