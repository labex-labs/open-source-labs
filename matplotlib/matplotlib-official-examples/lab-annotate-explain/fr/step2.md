# Connecter deux points avec une flèche

Dans cette étape, nous allons connecter les deux points avec une flèche. Nous utiliserons la fonction `annotate` pour créer la flèche et personnaliser le style et la couleur de la flèche.

```python
ax = axs.flat[0]
ax.plot([x1, x2], [y1, y2], ".")
ax.annotate("",
            xy=(x1, y1), xycoords='data',
            xytext=(x2, y2), textcoords='data',
            arrowprops=dict(arrowstyle="-",
                            color="0.5",
                            connectionstyle="arc3,rad=0.3",
                            ),
            )
```
