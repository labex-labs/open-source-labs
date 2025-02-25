# Setzen der großen und kleinen Markierungsgeber

```python
# Set the major locator
ax.xaxis.set_major_locator(MultipleLocator(20))
# Set the major formatter
ax.xaxis.set_major_formatter('{x:.0f}')
# Set the minor locator
ax.xaxis.set_minor_locator(MultipleLocator(5))
```

Hier legen wir den großen Markierungsgeber fest, um Markierungen in Vielfachen von 20 zu platzieren, legen den großen Formatierer fest, um die großen Markierungen mit der Formatierung ".0f" zu beschriften und legen den kleinen Markierungsgeber fest, um Markierungen in Vielfachen von 5 zu platzieren.
