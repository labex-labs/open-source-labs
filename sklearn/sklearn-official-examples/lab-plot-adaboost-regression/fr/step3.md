# Traçage des résultats

Enfin, nous traçons à quel point nos deux régresseurs, le régresseur d'arbre de décision unique et le régresseur AdaBoost, ont pu s'ajuster aux données. Nous utilisons la fonction `scatter()` de Matplotlib pour tracer les échantillons d'entraînement et les valeurs prédites par les deux régresseurs. Nous utilisons la fonction `plot()` de Matplotlib pour tracer les valeurs prédites en fonction des données pour les deux régresseurs. Nous ajoutons une légende au tracé pour distinguer les deux régresseurs.

```python
import matplotlib.pyplot as plt
import seaborn as sns

colors = sns.color_palette("colorblind")

plt.figure()
plt.scatter(X, y, color=colors[0], label="échantillons d'entraînement")
plt.plot(X, y_1, color=colors[1], label="n_estimators=1", linewidth=2)
plt.plot(X, y_2, color=colors[2], label="n_estimators=300", linewidth=2)
plt.xlabel("données")
plt.ylabel("cible")
plt.title("Régression par arbre de décision amélioré")
plt.legend()
plt.show()
```
