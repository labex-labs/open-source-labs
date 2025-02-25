# Festlegen der Diagrammgrenzen und -beschriftungen

Schließlich legen wir die Diagrammgrenzen und -beschriftungen mit der `set`-Funktion fest.

```python
ax.set(xlim=(0, 10), ylim=(1, 9), zlim=(0, 0.35),
       xlabel='x', ylabel=r'$\lambda$', zlabel='Wahrscheinlichkeit')
```
