# Créer le diagramme en forme d'arête de poisson

Maintenant, nous allons créer le diagramme en forme d'arête de poisson. Nous commencerons par créer un objet figure et un objet axe.

```python
fig, ax = plt.subplots(figsize=(10, 6), layout='constrained')
```

Ensuite, nous définirons les limites x et y de l'axe et désactiverons l'axe.

```python
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.axis('off')
```
