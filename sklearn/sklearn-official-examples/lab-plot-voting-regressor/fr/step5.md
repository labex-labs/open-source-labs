# Tracer les résultats

Enfin, nous allons visualiser les 20 prédictions. Les étoiles rouges montrent la prédiction moyenne effectuée par le Voting Regressor.

```python
# Plot the results
plt.figure()
plt.plot(pred1, "gd", label="GradientBoostingRegressor")
plt.plot(pred2, "b^", label="RandomForestRegressor")
plt.plot(pred3, "ys", label="LinearRegression")
plt.plot(pred4, "r*", ms=10, label="VotingRegressor")

plt.tick_params(axis="x", which="both", bottom=False, top=False, labelbottom=False)
plt.ylabel("prédit")
plt.xlabel("échantillons d'entraînement")
plt.legend(loc="best")
plt.title("Prédictions des régresseurs et leur moyenne")

plt.show()
```
