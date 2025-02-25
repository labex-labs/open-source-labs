# Tracez un cercle avec un rapport d'aspect d'axes égal

Pour définir le rapport d'aspect d'axes égal, nous pouvons utiliser la fonction `axis('equal')`.

```python
axs[0, 1].plot(3 * np.cos(an), 3 * np.sin(an))
axs[0, 1].axis('equal')
axs[0, 1].set_title('equal, looks like circle', fontsize=10)
```

La courbe résultante montrera un cercle qui est proportionnel et visuellement attrayant.
