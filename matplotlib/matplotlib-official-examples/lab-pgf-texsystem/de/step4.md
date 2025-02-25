# Text zum Plot hinzufügen

Du kannst Text zu deinem Plot hinzufügen, indem du die Funktion `ax.text()` verwendest. In diesem Beispiel werden wir Text mit verschiedenen Schriftfamilien hinzufügen.

```python
ax.text(0.5, 3., "serif", family="serif")
ax.text(0.5, 2., "monospace", family="monospace")
ax.text(2.5, 2., "sans-serif", family="sans-serif")
ax.set_xlabel(r"µ ist nicht $\mu$")
```
