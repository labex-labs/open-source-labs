# Erstelle die Subplots

Wir werden eine Figur mit zwei Subplots mithilfe von `.pyplot.subplot` erstellen.

```python
plt.figure()

plt.subplot(211)
plt.plot(t1, f(t1), color='tab:blue', marker='o')
plt.plot(t2, f(t2), color='black')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), color='tab:orange', linestyle='--')

plt.show()
```

Die `subplot()`-Funktion nimmt drei Argumente entgegen: die Anzahl der Zeilen, die Anzahl der Spalten und den Index des aktuellen Plots. Der Index beginnt in der oberen linken Ecke bei 1 und erhöht sich zeilenweise. In diesem Beispiel erstellen wir eine Figur mit zwei Subplots: einen oben und einen unten.

Im ersten Subplot plotten wir `t1` gegen `f(t1)` und `t2` gegen `f(t2)`. Wir setzen die Farbe des ersten Plots auf blau und fügen kreisförmige Marker zu jedem Datenpunkt hinzu. Wir setzen die Farbe des zweiten Plots auf schwarz.

Im zweiten Subplot plotten wir `t2` gegen die Kosinusfunktion von `2*np.pi*t2`. Wir setzen die Farbe des Plots auf orange und den Linienstil auf gestrichelt.
