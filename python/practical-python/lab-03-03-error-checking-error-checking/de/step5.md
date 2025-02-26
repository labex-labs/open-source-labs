# Ausnahmewerte

Ausnahmen haben einen zugeordneten Wert. Er enthält genauere Informationen darüber, was schiefgeht.

```python
raise RuntimeError('Invalid user name')
```

Dieser Wert ist Teil der Ausnahmeinstanz, die in die Variable eingefügt wird, die an `except` übergeben wird.

```python
try:
 ...
except RuntimeError as e:   # `e` hält die ausgelöste Ausnahme
 ...
```

`e` ist eine Instanz des Ausnahmetyps. Wenn es aber gedruckt wird, sieht es oft wie eine Zeichenkette aus.

```python
except RuntimeError as e:
    print('Failed : Reason', e)
```
