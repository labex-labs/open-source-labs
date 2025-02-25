# Erstellen einer Formatierungsfunktion

Wir erstellen eine Formatierungsfunktion, die das Tick-Label aus dem Wert an der Markierung bestimmt. Wenn der Tick-Wert eine Ganzzahl im Bereich von `xs` ist, wird das entsprechende Label aus der `labels`-Liste zurückgegeben. Andernfalls wird ein leerer String zurückgegeben.

```python
def format_fn(tick_val, tick_pos):
    if int(tick_val) in xs:
        return labels[int(tick_val)]
    else:
        return ''
```
