# Tracer les résultats

Dans cette étape, nous allons tracer les résultats. Nous utiliserons `matplotlib.pyplot` pour créer un graphique à points dispersés des données originales et de chaque prédiction des trois modèles. Nous ajouterons également des étiquettes et un titre au graphique.

```python
# Plot the results
plt.figure()
s = 25
plt.scatter(y[:, 0], y[:, 1], c="navy", s=s, edgecolor="black", label="données")
plt.scatter(
    y_1[:, 0],
    y_1[:, 1],
    c="cornflowerblue",
    s=s,
    edgecolor="black",
    label="profondeur maximale = 2",
)
plt.scatter(y_2[:, 0], y_2[:, 1], c="rouge", s=s, edgecolor="black", label="profondeur maximale = 5")
plt.scatter(
    y_3[:, 0], y_3[:, 1], c="orange", s=s, edgecolor="black", label="profondeur maximale = 8"
)
plt.xlim([-6, 6])
plt.ylim([-6, 6])
plt.xlabel("cible 1")
plt.ylabel("cible 2")
plt.title("Régression arborescente à sortie multiple")
plt.legend(loc="meilleur")
plt.show()
```
