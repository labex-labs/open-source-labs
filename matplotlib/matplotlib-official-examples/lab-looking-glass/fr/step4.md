# Traçage des données

Nous allons tracer les données aléatoires générées dans l'Étape 2 à l'aide de la fonction `plot()` deux fois. Le premier tracé aura une valeur d'alpha de 0,2 et le second tracé aura une valeur d'alpha de 1,0 et une zone de découpe définie sur le patch de cercle jaune.

```python
ax.plot(x, y, alpha=0.2)
line, = ax.plot(x, y, alpha=1.0, clip_path=circ)
ax.set_title("Left click and drag to move looking glass")
```
