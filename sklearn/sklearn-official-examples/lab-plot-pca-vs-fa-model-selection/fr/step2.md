# Ajuster les modèles

Nous allons ajuster les modèles de PCA probabiliste et d'analyse factorielle à l'ensemble de données, et utiliser la validation croisée pour évaluer leur performance. Nous allons également calculer les scores pour les estimateurs de covariance à rétrécissement, et comparer les résultats.

```python
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA, FactorAnalysis
from sklearn.covariance import ShrunkCovariance, LedoitWolf
from sklearn.model_selection import cross_val_score, GridSearchCV

n_components = np.arange(0, n_features, 5)  # options pour n_components

def compute_scores(X):
    pca = PCA(svd_solver="full")
    fa = FactorAnalysis()

    pca_scores, fa_scores = [], []
    for n in n_components:
        pca.n_components = n
        fa.n_components = n
        pca_scores.append(np.mean(cross_val_score(pca, X)))
        fa_scores.append(np.mean(cross_val_score(fa, X)))

    return pca_scores, fa_scores

def shrunk_cov_score(X):
    shrinkages = np.logspace(-2, 0, 30)
    cv = GridSearchCV(ShrunkCovariance(), {"shrinkage": shrinkages})
    return np.mean(cross_val_score(cv.fit(X).best_estimator_, X))

def lw_score(X):
    return np.mean(cross_val_score(LedoitWolf(), X))

for X, title in [(X_homo, "Bruit homoscédaastique"), (X_hetero, "Bruit hétéroscédaastique")]:
    pca_scores, fa_scores = compute_scores(X)
    n_components_pca = n_components[np.argmax(pca_scores)]
    n_components_fa = n_components[np.argmax(fa_scores)]

    pca = PCA(svd_solver="full", n_components="mle")
    pca.fit(X)
    n_components_pca_mle = pca.n_components_

    print("meilleur n_components par validation croisée PCA = %d" % n_components_pca)
    print("meilleur n_components par validation croisée FactorAnalysis = %d" % n_components_fa)
    print("meilleur n_components par estimation maximale de vraisemblance PCA = %d" % n_components_pca_mle)

    plt.figure()
    plt.plot(n_components, pca_scores, "b", label="Scores PCA")
    plt.plot(n_components, fa_scores, "r", label="Scores FA")
    plt.axvline(rank, color="g", label="VRAI: %d" % rank, linestyle="-")
    plt.axvline(
        n_components_pca,
        color="b",
        label="Validation croisée PCA: %d" % n_components_pca,
        linestyle="--",
    )
    plt.axvline(
        n_components_fa,
        color="r",
        label="Validation croisée FactorAnalysis: %d" % n_components_fa,
        linestyle="--",
    )
    plt.axvline(
        n_components_pca_mle,
        color="k",
        label="Estimation maximale de vraisemblance PCA: %d" % n_components_pca_mle,
        linestyle="--",
    )

    # comparer avec d'autres estimateurs de covariance
    plt.axhline(
        shrunk_cov_score(X),
        color="violet",
        label="Estimation maximale de vraisemblance de covariance rétrécie",
        linestyle="-.",
    )
    plt.axhline(
        lw_score(X),
        color="orange",
        label="Estimation maximale de vraisemblance de LedoitWolf %d" % n_components_pca_mle,
        linestyle="-.",
    )

    plt.xlabel("nombre de composantes")
    plt.ylabel("Scores de validation croisée")
    plt.legend(loc="bas droite")
    plt.title(title)

plt.show()
```
