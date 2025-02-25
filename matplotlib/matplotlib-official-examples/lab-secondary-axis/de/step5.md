# Erstellen der sekundären X-Achse

Wir werden die sekundäre X-Achse erstellen und die Umrechnung von Frequenz in Periode durchführen. Wir werden `one_over` als die Vorwärtsfunktion und `inverse` als die Umkehrfunktion verwenden.

```python
def one_over(x):
    """Vektorisiertes 1/x, wobei x==0 manuell behandelt wird"""
    x = np.array(x, float)
    near_zero = np.isclose(x, 0)
    x[near_zero] = np.inf
    x[~near_zero] = 1 / x[~near_zero]
    return x

# die Funktion "1/x" ist ihre eigene Umkehrfunktion
inverse = one_over

secax = ax.secondary_xaxis('top', functions=(one_over, inverse))
secax.set_xlabel('period [s]')
```
