# Ajouter une annotation avec une forme

Les formes peuvent être utilisées pour attirer l'attention sur des régions spécifiques d'un graphique. Dans cette étape, nous allons ajouter un rectangle pour souligner la zone comprise entre x = 1 et x = 3.

```python
# Add shape annotation
ax.axvspan(1, 3, facecolor='gray', alpha=0.2)
plt.show()
```
