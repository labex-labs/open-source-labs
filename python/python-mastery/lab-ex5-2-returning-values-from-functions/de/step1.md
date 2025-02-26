# Rückgabe mehrerer Werte

Angenommen, Sie schreiben Code, um Konfigurationsdateien zu analysieren, die Zeilen wie diese enthalten:

    name=value

Schreiben Sie eine Funktion `parse_line(line)`, die eine solche Zeile annimmt und sowohl den zugehörigen Namen als auch den Wert zurückgibt. Die übliche Konvention für die Rückgabe mehrerer Werte besteht darin, sie in einem Tupel zurückzugeben. Beispielsweise:

```python
>>> parse_line('email=guido@python.org')
('email', 'guido@python.org')
>>> name, val = parse_line('email=guido@python.org')
>>> name
'email'
>>> val
'guido@python.org'
>>>
```
