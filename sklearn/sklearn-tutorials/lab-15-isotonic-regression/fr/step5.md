# Visualisez les résultats

Enfin, visualisons les résultats de notre modèle de régression isotone. Nous pouvons tracer les points de données d'origine sous forme de points de dispersion et les valeurs prédites sous forme d'une ligne.

```python
import matplotlib.pyplot as plt

# Trace les données d'origine et les valeurs prédites
plt.scatter(X, y, c='b', label='Données d\'origine')
plt.plot(X_new, y_pred, c='r', label='Régression isotone')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
```
