# Erstellen der Figur und der Achsen

Wir werden ein Figurenobjekt erstellen und einer einzigen Achsenmenge hinzufügen. Wir werden auch den Titel der Grafik festlegen.

```python
fig = plt.figure(figsize=(8, 9))
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[],
                     title="Rankine Power Cycle: Example 8.6 from Moran and "
                     "Shapiro\n\x22Fundamentals of Engineering Thermodynamics "
                     "\x22, 6th ed., 2008")
```
