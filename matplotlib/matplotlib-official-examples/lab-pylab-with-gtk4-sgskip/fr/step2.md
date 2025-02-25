# Créez la figure et les tracés

```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3], 'ro-', label='easy as 1 2 3')
ax.plot([1, 4, 9], 'gs--', label='easy as 1 2 3 squared')
ax.legend()
```

Nous créons une figure avec deux sous-graphiques et traçons deux ensembles de données dessus. Nous ajoutons également une légende aux tracés.
