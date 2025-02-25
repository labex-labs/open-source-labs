# Die Achsen invertieren

Um die x-Achse zu invertieren, müssen wir einfach die Reihenfolge der Grenzen mit der `set_xlim`-Funktion umkehren. In diesem Beispiel setzen wir die Grenzen der x-Achse von 5 bis 0, was die x-Achse effektiv umkehrt.

```python
ax.set_xlim(5, 0)  # abnehmende Zeit
```
