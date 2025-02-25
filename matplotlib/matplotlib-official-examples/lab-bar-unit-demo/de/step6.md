# Füge Beschriftungen und Titel zum Diagramm hinzu

Der letzte Schritt besteht darin, Beschriftungen und einen Titel zum Diagramm hinzuzufügen. Wir werden einen Titel zum Diagramm, eine Beschriftung für die x-Achse und eine Legende für das Diagramm hinzufügen.

```python
ax.set_title('Cup height by group and beverage choice')
ax.set_xlabel('Group')
ax.legend()
ax.autoscale_view()
```
