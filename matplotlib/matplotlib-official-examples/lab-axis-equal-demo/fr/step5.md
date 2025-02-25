# Ajustement automatique des limites de données pour un rapport d'aspect d'axes égal

Nous pouvons également utiliser la fonction `set_aspect('equal', 'box')` pour ajuster automatiquement les limites de données pour un rapport d'aspect d'axes égal.

```python
axs[1, 1].plot(3 * np.cos(an), 3 * np.sin(an))
axs[1, 1].set_aspect('equal', 'box')
axs[1, 1].set_title('still a circle, auto-adjusted data limits', fontsize=10)
```

Le tracé résultant montrera un cercle qui est toujours proportionnel et visuellement attrayant.
