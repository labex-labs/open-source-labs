# Ajustar os Modelos

Ajustaremos os modelos PCA Probabilístico e Análise Fatorial ao conjunto de dados e usaremos validação cruzada para avaliar seu desempenho. Também calcularemos as pontuações para estimadores de covariância de encolhimento e compararemos os resultados.

```python
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA, FactorAnalysis
from sklearn.covariance import ShrunkCovariance, LedoitWolf
from sklearn.model_selection import cross_val_score, GridSearchCV

n_components = np.arange(0, n_features, 5)  # opções para n_components

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

for X, title in [(X_homo, "Ruído Homocedástico"), (X_hetero, "Ruído Heterocedástico")]:
    pca_scores, fa_scores = compute_scores(X)
    n_components_pca = n_components[np.argmax(pca_scores)]
    n_components_fa = n_components[np.argmax(fa_scores)]

    pca = PCA(svd_solver="full", n_components="mle")
    pca.fit(X)
    n_components_pca_mle = pca.n_components_

    print("melhor n_components por PCA CV = %d" % n_components_pca)
    print("melhor n_components por AnáliseFatorial CV = %d" % n_components_fa)
    print("melhor n_components por PCA MLE = %d" % n_components_pca_mle)

    plt.figure()
    plt.plot(n_components, pca_scores, "b", label="Pontuações PCA")
    plt.plot(n_components, fa_scores, "r", label="Pontuações AF")
    plt.axvline(rank, color="g", label="VERDADE: %d" % rank, linestyle="-")
    plt.axvline(
        n_components_pca,
        color="b",
        label="PCA CV: %d" % n_components_pca,
        linestyle="--",
    )
    plt.axvline(
        n_components_fa,
        color="r",
        label="AnáliseFatorial CV: %d" % n_components_fa,
        linestyle="--",
    )
    plt.axvline(
        n_components_pca_mle,
        color="k",
        label="PCA MLE: %d" % n_components_pca_mle,
        linestyle="--",
    )

    # comparar com outros estimadores de covariância
    plt.axhline(
        shrunk_cov_score(X),
        color="violet",
        label="Covariância Encolhida MLE",
        linestyle="-.",
    )
    plt.axhline(
        lw_score(X),
        color="orange",
        label="LedoitWolf MLE",
        linestyle="-.",
    )

    plt.xlabel("número de componentes")
    plt.ylabel("Pontuações CV")
    plt.legend(loc="inferior direita")
    plt.title(title)

plt.show()
```
