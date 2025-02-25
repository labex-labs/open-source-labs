# Die Daten plotten

In diesem Schritt werden wir die `plot`-Funktion in Matplotlib verwenden, um alle drei Datensätze in einem einzelnen Aufruf zu plotten. Wir werden für den ersten Datensatz rote Striche, für den zweiten Datensatz blaue Quadrate und für den dritten Datensatz grüne Dreiecke verwenden.

```python
plt.plot(t, t, 'r--', label='linear')
plt.plot(t, t**2, 'bs', label='quadratic')
plt.plot(t, t**3, 'g^', label='cubic')
plt.legend()
plt.show()
```
