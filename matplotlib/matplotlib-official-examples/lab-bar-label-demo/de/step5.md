# Balkenbeschriftung mit `{}`-stiligem Formatstring

In diesem Schritt zeigen wir, wie ein `{}`-stiliger Formatstring verwendet werden kann, um Balkenbeschriftungen zu formatieren. Wir verwenden einige Daten über die Verkaufszahlen von Gelato nach Geschmack.

```python
fruit_names = ['Coffee', 'Salted Caramel', 'Pistachio']
fruit_counts = [4000, 2000, 7000]

fig, ax = plt.subplots()
bar_container = ax.bar(fruit_names, fruit_counts)
ax.set(ylabel='pints sold', title='Gelato sales by flavor', ylim=(0, 8000))
ax.bar_label(bar_container, fmt='{:,.0f}')
```
