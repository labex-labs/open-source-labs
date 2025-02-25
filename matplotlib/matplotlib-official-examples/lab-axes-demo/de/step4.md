# Einfachachsen erstellen

In diesem Schritt erstellen wir zwei Einfachachsen innerhalb der Hauptdiagrammachsen mit `fig.add_axes`. Eine wird ein Histogramm der Daten anzeigen, und die andere wird die Impulsantwort anzeigen.

```python
# Create right inset axes
right_inset_ax = fig.add_axes([.65,.6,.2,.2], facecolor='k')
right_inset_ax.hist(s, 400, density=True)
right_inset_ax.set(title='Wahrscheinlichkeit', xticks=[], yticks=[])

# Create left inset axes
left_inset_ax = fig.add_axes([.2,.6,.2,.2], facecolor='k')
left_inset_ax.plot(t[:len(r)], r)
left_inset_ax.set(title='Impulsantwort', xlim=(0,.2), xticks=[], yticks=[])
```
