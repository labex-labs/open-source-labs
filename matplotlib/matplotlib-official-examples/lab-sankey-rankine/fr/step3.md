# Créez la figure et les axes

Nous allons créer un objet figure et y ajouter un seul ensemble d'axes. Nous allons également définir le titre du tracé.

```python
fig = plt.figure(figsize=(8, 9))
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[],
                     title="Rankine Power Cycle: Example 8.6 from Moran and "
                     "Shapiro\n\x22Fundamentals of Engineering Thermodynamics "
                     "\x22, 6th ed., 2008")
```
