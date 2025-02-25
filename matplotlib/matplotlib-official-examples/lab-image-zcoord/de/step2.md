# Erstellen einer Zufallsmatrix

Als nächstes werden wir mit numpy eine Zufallsmatrix erstellen. Wir werden die `rand`-Methode verwenden, um eine 5x3-Matrix mit Zufallswerten zwischen 0 und 1 zu erstellen. Wir setzen auch einen Zufallszahlengenerator, um die Reproduzierbarkeit der Ergebnisse zu gewährleisten.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

X = 10*np.random.rand(5, 3)
```
