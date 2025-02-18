# Erstellen des unterbrochenen horizontalen Balkendiagramms

In diesem Schritt werden wir das unterbrochene horizontale Balkendiagramm erstellen. Wir werden die Methode `broken_barh()` der Klasse `Axes` verwenden, um das Diagramm zu erstellen. Die Methode `broken_barh()` nimmt drei Argumente entgegen: Das erste Argument ist eine Liste von Tupeln, wobei jedes Tupel ein Segment des Balkens darstellt. Das erste Element des Tupels ist der Startpunkt des Segments, und das zweite Element ist die Länge des Segments. Das zweite Argument ist die y-Koordinate des Balkens, und das dritte Argument ist die Füllfarbe des Balkens.

```python
fig, ax = plt.subplots()
ax.broken_barh([(110, 30), (150, 10)], (10, 9), facecolors='tab:blue')
ax.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9),
               facecolors=('tab:orange', 'tab:green', 'tab:red'))
ax.set_ylim(5, 35)
ax.set_xlim(0, 200)
ax.set_xlabel('seconds since start')
ax.set_yticks([15, 25], labels=['Bill', 'Jim'])
ax.grid(True)
ax.annotate('race interrupted', (61, 25),
            xytext=(0.8, 0.9), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=16,
            horizontalalignment='right', verticalalignment='top')

plt.show()
```
