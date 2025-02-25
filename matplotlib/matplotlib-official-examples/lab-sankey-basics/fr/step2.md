# Créer un diagramme Sankey simple

Nous allons commencer par créer un diagramme Sankey simple qui montre comment utiliser la classe Sankey.

```python
Sankey(flows=[0.25, 0.15, 0.60, -0.20, -0.15, -0.05, -0.50, -0.10],
       labels=['', '', '', 'Premier', 'Second', 'Troisième', 'Quatrième', 'Cinquième'],
       orientations=[-1, 1, 0, 1, 1, 1, 0, -1]).finish()
plt.title("Les paramètres par défaut produisent un diagramme comme celui-ci.")
```

Ce code produira un diagramme Sankey avec les paramètres par défaut, qui incluent les étiquettes et les orientations des flux. Le diagramme résultant sera affiché avec le titre "Les paramètres par défaut produisent un diagramme comme celui-ci."
