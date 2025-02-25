# Utiliser le style de boîte personnalisé

Une fois que vous avez implémenté et enregistré un style de boîte personnalisé, vous pouvez l'utiliser avec `Axes.text`.

```python
fig, ax = plt.subplots(figsize=(3, 3))
ax.text(0.5, 0.5, "Test", size=30, va="center", ha="center", rotation=30,
        bbox=dict(boxstyle="angled,pad=0.5", alpha=0.2))
```
