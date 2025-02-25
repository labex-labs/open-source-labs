# Anpassen der Grenzen und Hinzufügen von Beschriftungen

Schließlich werden wir die Grenzen des Diagramms anpassen und Achsenbeschriftungen hinzufügen, indem wir die Funktionen `set_zlim()`, `set_xlabel()`, `set_ylabel()` und `set_zlabel()` von Matplotlib verwenden. Wir werden auch die LaTeX-Math-Mode verwenden, um die Achsenbeschriftungen zu schreiben.

```python
ax.set_zlim(0, 1)
ax.set_xlabel(r'$\phi_\mathrm{real}$')
ax.set_ylabel(r'$\phi_\mathrm{im}$')
ax.set_zlabel(r'$V(\phi)$')
```
