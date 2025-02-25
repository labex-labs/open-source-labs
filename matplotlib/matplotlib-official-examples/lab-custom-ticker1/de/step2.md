# Definiere benutzerdefinierte Ticker-Funktion

Als nächstes müssen wir die benutzerdefinierte Ticker-Funktion definieren. Die benutzerdefinierte Ticker-Funktion nimmt zwei Argumente entgegen - den Wert und die Tick-Position - und gibt das formatierte Tick-Label zurück. In diesem Fall werden wir das Tick-Label als Dollar in Millionen formatieren.

```python
def millions(x, pos):
    """Die beiden Argumente sind der Wert und die Tick-Position."""
    return f'${x*1e-6:1.1f}M'
```
