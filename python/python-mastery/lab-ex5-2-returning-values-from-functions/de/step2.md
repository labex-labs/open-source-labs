# Rückgabe optionaler Werte

Manchmal kann eine Funktion einen optionalen Wert zurückgeben - möglicherweise als Mechanismus, um Erfolg oder Misserfolg anzuzeigen. Die am häufigsten verwendete Konvention besteht darin, `None` als Darstellung für einen fehlenden Wert zu verwenden. Ändern Sie die obige Funktion `parse_line()`, so dass sie entweder ein Tupel bei Erfolg oder `None` bei ungültigen Daten zurückgibt. Beispielsweise:

```python
>>> parse_line('email=guido@python.org')
('email', 'guido@python.org')
>>> parse_line('spam')       # Gibt None zurück
>>>
```

Design-Diskussion: Würde es besser sein, wenn die Funktion `parse_line()` eine Ausnahme bei fehlerhaften Daten auslöst?
