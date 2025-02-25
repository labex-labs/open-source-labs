# Personnalisez les annotations

Nous pouvons personnaliser les annotations en changeant la taille de police, la couleur de police et le style de flèche. Le code suivant changera la taille de police, la couleur de police et le style de flèche de l'annotation de texte.

```python
ax.annotate("Point de données 1", xy=(1, 3), xytext=(1.5, 3.5),
            arrowprops=dict(facecolor="black", shrink=0.05, arrowstyle="->"),
            fontsize=12, color="red")
```
