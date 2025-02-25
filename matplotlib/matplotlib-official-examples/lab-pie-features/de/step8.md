# Die Größe steuern

Wir können die Größe des Kreisdiagramms steuern, indem wir den `radius`-Parameter der `pie()`-Funktion festlegen.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%.0f%%',
       textprops={'size':'smaller'}, radius=0.5)
```
