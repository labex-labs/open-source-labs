# Visualiser les classements des caractéristiques

Enfin, nous allons tracer les classements des caractéristiques à l'aide de la bibliothèque Matplotlib. Nous utiliserons la fonction `matshow()` pour afficher les classements sous forme d'image. Nous ajouterons également une barre de couleur et un titre au graphique.

```python
import matplotlib.pyplot as plt

plt.matshow(ranking, cmap=plt.cm.Blues)
plt.colorbar()
plt.title("Ranking of pixels with RFE")
plt.show()
```
