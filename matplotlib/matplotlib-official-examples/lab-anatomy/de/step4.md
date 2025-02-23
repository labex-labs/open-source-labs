# Beschriftungen und Titel hinzufügen

Wir werden nun Beschriftungen für die x- und y-Achsen hinzufügen und einen Titel für die Figur mit den Methoden `set_xlabel()`, `set_ylabel()` und `set_title()` setzen.

```python
# Add labels and title
ax.set_xlabel("x-Achsenbeschriftung", fontsize=14)
ax.set_ylabel("y-Achsenbeschriftung", fontsize=14)
ax.set_title("Anatomie einer Figur", fontsize=20, verticalalignment='bottom')
```
