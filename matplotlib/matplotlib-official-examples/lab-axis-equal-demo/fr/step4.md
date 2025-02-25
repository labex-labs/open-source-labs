# Ajustez les limites du tracé tout en conservant le rapport d'aspect d'axes égal

Nous pouvons également ajuster les limites du tracé tout en conservant le rapport d'aspect d'axes égal.

```python
axs[1, 0].plot(3 * np.cos(an), 3 * np.sin(an))
axs[1, 0].axis('equal')
axs[1, 0].set(xlim=(-3, 3), ylim=(-3, 3))
axs[1, 0].set_title('still a circle, even after changing limits', fontsize=10)
```

Le tracé résultant montrera un cercle qui est toujours proportionnel même après avoir changé les limites.
