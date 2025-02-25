# Definieren einer Funktion zur Umrechnung von Fahrenheit in Celsius

Als nächstes definieren wir eine Funktion, um die Temperatur in Fahrenheit in Celsius umzurechnen.

```python
def fahrenheit2celsius(temp):
    """
    Gibt die Temperatur in Celsius zurück, wenn die Fahrenheit-Temperatur angegeben ist.
    """
    return (5. / 9.) * (temp - 32)
```
