# Das Diagramm anpassen

Wir können das Aussehen unseres Diagramms anpassen, indem wir Beschriftungen für die x-Achse und die y-Achse hinzufügen und die Skala der y-Achse auf logarithmisch setzen.

```python
ax.set_xticks(x + dimw / 2, labels=map(str, x))
ax.set_yscale('log')

ax.set_xlabel('x')
ax.set_ylabel('y')
```
