# Bornes théoriques (suite)

Le second graphique montre qu'une augmentation de la distorsion admissible `eps` permet de réduire le nombre minimal de dimensions `n_components` pour un nombre donné d'échantillons `n_samples`.

```python
# plage de distorsions admissibles
eps_range = np.linspace(0.01, 0.99, 100)

# plage du nombre d'échantillons (observations) à plonger
n_samples_range = np.logspace(2, 6, 5)
couleurs = plt.cm.Blues(np.linspace(0.3, 1.0, len(n_samples_range)))

plt.figure()
for n_samples, couleur in zip(n_samples_range, couleurs):
    min_n_components = johnson_lindenstrauss_min_dim(n_samples, eps=eps_range)
    plt.semilogy(eps_range, min_n_components, couleur=couleur)

plt.legend([f"n_samples = {n}" for n in n_samples_range], loc="haut droite")
plt.xlabel("Distorsion eps")
plt.ylabel("Nombre minimum de dimensions")
plt.title("Bornes de Johnson-Lindenstrauss :\nn_components vs eps")
plt.show()
```
