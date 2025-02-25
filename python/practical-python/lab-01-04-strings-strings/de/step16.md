# Übung 1.17: f-Strings

Manchmal möchten Sie einen String erstellen und die Werte von Variablen darin einfügen.

Um das zu tun, verwenden Sie einen f-String. Beispielsweise:

```python
>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> f'{shares} shares of {name} at ${price:0.2f}'
'100 shares of IBM at $91.10'
>>>
```

Ändern Sie das `mortgage.py`-Programm aus Übung 1.10, um seine Ausgabe mit f-Strings zu erstellen. Versuchen Sie, es so zu gestalten, dass die Ausgabe gut ausgerichtet ist.
