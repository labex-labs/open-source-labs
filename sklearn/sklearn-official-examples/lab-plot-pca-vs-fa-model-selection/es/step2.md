# Ajustar los modelos

Ajustaremos los modelos de PCA Probabilístico y Análisis Factorial al conjunto de datos y usaremos validación cruzada para evaluar su rendimiento. También computaremos las puntuaciones para los estimadores de covarianza de encogimiento y compararemos los resultados.

```python
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA, FactorAnalysis
from sklearn.covariance import ShrunkCovariance, LedoitWolf
from sklearn.model_selection import cross_val_score, GridSearchCV

n_components = np.arange(0, n_features, 5)  # opciones para n_components

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

for X, title in [(X_homo, "Ruido Homoscedástico"), (X_hetero, "Ruido Heteroscedástico")]:
    pca_scores, fa_scores = compute_scores(X)
    n_components_pca = n_components[np.argmax(pca_scores)]
    n_components_fa = n_components[np.argmax(fa_scores)]

    pca = PCA(svd_solver="full", n_components="mle")
    pca.fit(X)
    n_components_pca_mle = pca.n_components_

    print("mejor n_components por CV de PCA = %d" % n_components_pca)
    print("mejor n_components por CV de FactorAnalysis = %d" % n_components_fa)
    print("mejor n_components por MLE de PCA = %d" % n_components_pca_mle)

    plt.figure()
    plt.plot(n_components, pca_scores, "b", label="Puntuaciones de PCA")
    plt.plot(n_components, fa_scores, "r", label="Puntuaciones de FA")
    plt.axvline(rank, color="g", label="VERDAD: %d" % rank, linestyle="-")
    plt.axvline(
        n_components_pca,
        color="b",
        label="PCA CV: %d" % n_components_pca,
        linestyle="--",
    )
    plt.axvline(
        n_components_fa,
        color="r",
        label="FactorAnalysis CV: %d" % n_components_fa,
        linestyle="--",
    )
    plt.axvline(
        n_components_pca_mle,
        color="k",
        label="PCA MLE: %d" % n_components_pca_mle,
        linestyle="--",
    )

    # comparar con otros estimadores de covarianza
    plt.axhline(
        shrunk_cov_score(X),
        color="violeta",
        label="MLE de Covarianza Encogida",
        linestyle="-.",
    )
    plt.axhline(
        lw_score(X),
        color="naranja",
        label="MLE de LedoitWolf %d" % n_components_pca_mle,
        linestyle="-.",
    )

    plt.xlabel("número de componentes")
    plt.ylabel("Puntuaciones de CV")
    plt.legend(loc="inferior derecha")
    plt.title(title)

plt.show()
```
