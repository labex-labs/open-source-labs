# Codage sparse

Nous allons effectuer un codage sparse sur le signal en utilisant différentes méthodes et visualiser les résultats.

```python
# Liste les différentes méthodes de codage sparse dans le format suivant :
# (titre, transform_algorithm, transform_alpha,
#  transform_n_nozero_coefs, couleur)
estimators = [
    ("OMP", "omp", None, 15, "navy"),
    ("Lasso", "lasso_lars", 2, None, "turquoise"),
]
lw = 2

plt.figure(figsize=(13, 6))
for subplot, (D, titre) in enumerate(
    zip((D_fixed, D_multi), ("largeur fixe", "plusieurs largeurs"))
):
    plt.subplot(1, 2, subplot + 1)
    plt.title("Codage sparse contre le dictionnaire %s" % titre)
    plt.plot(y, lw=lw, linestyle="--", label="Signal original")
    # Effectuez une approximation d'ondelette
    for titre, algo, alpha, n_nonzero, couleur in estimators:
        coder = SparseCoder(
            dictionary=D,
            transform_n_nonzero_coefs=n_nonzero,
            transform_alpha=alpha,
            transform_algorithm=algo,
        )
        x = coder.transform(y.reshape(1, -1))
        densité = len(np.flatnonzero(x))
        x = np.ravel(np.dot(x, D))
        erreur_carrée = np.sum((y - x) ** 2)
        plt.plot(
            x,
            color=couleur,
            lw=lw,
            label="%s : %s coefficients non nuls,\n%.2f d'erreur" % (titre, densité, erreur_carrée),
        )

    # Désajustement par seuillage doux
    coder = SparseCoder(
        dictionary=D, transform_algorithm="threshold", transform_alpha=20
    )
    x = coder.transform(y.reshape(1, -1))
    _, idx = np.where(x!= 0)
    x[0, idx], _, _, _ = np.linalg.lstsq(D[idx, :].T, y, rcond=None)
    x = np.ravel(np.dot(x, D))
    erreur_carrée = np.sum((y - x) ** 2)
    plt.plot(
        x,
        color="darkorange",
        lw=lw,
        label="Seuillage avec désajustement :\n%d coefficients non nuls, %.2f d'erreur"
        % (len(idx), erreur_carrée),
    )
    plt.axis("tight")
    plt.legend(shadow=False, loc="best")
plt.subplots_adjust(0.04, 0.07, 0.97, 0.90, 0.09, 0.2)
plt.show()
```
