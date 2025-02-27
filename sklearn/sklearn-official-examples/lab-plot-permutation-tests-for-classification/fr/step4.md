# Tracer les résultats

Nous traçons un histogramme des scores de permutation (la distribution nulle) pour le jeu de données iris original et les données aléatorisées. Nous indiquons également le score obtenu par le classifieur sur les données originales en utilisant une ligne rouge. La valeur p est affichée sur chaque graphique.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# Données originales
ax.hist(perm_scores_iris, bins=20, density=True)
ax.axvline(score_iris, ls="--", color="r")
score_label = f"Score sur les données originales : {score_iris:.2f}\n(p-valeur : {pvalue_iris:.3f})"
ax.text(0.7, 10, score_label, fontsize=12)
ax.set_xlabel("Score de précision")
_ = ax.set_ylabel("Densité de probabilité")

plt.show()

fig, ax = plt.subplots()

# Données aléatoires
ax.hist(perm_scores_rand, bins=20, density=True)
ax.set_xlim(0.13)
ax.axvline(score_rand, ls="--", color="r")
score_label = f"Score sur les données originales : {score_rand:.2f}\n(p-valeur : {pvalue_rand:.3f})"
ax.text(0.14, 7.5, score_label, fontsize=12)
ax.set_xlabel("Score de précision")
ax.set_ylabel("Densité de probabilité")

plt.show()
```
