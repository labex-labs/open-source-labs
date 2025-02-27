# Настройка моделей

Мы настроим модели Probabilistic PCA и Factor Analysis на датасет и используем кросс-валидацию для оценки их производительности. Также вычислим оценки для сжатия ковариационных оценщиков и сравним результаты.

```python
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA, FactorAnalysis
from sklearn.covariance import ShrunkCovariance, LedoitWolf
from sklearn.model_selection import cross_val_score, GridSearchCV

n_components = np.arange(0, n_features, 5)  # варианты для n_components

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

for X, title in [(X_homo, "Гомоскедастический шум"), (X_hetero, "Гетероскедастический шум")]:
    pca_scores, fa_scores = compute_scores(X)
    n_components_pca = n_components[np.argmax(pca_scores)]
    n_components_fa = n_components[np.argmax(fa_scores)]

    pca = PCA(svd_solver="full", n_components="mle")
    pca.fit(X)
    n_components_pca_mle = pca.n_components_

    print("лучшее n_components по кросс-валидации PCA = %d" % n_components_pca)
    print("лучшее n_components по кросс-валидации FactorAnalysis = %d" % n_components_fa)
    print("лучшее n_components по PCA MLE = %d" % n_components_pca_mle)

    plt.figure()
    plt.plot(n_components, pca_scores, "b", label="Оценки PCA")
    plt.plot(n_components, fa_scores, "r", label="Оценки FA")
    plt.axvline(rank, color="g", label="ПРАВДА: %d" % rank, linestyle="-")
    plt.axvline(
        n_components_pca,
        color="b",
        label="PCA кросс-валидация: %d" % n_components_pca,
        linestyle="--",
    )
    plt.axvline(
        n_components_fa,
        color="r",
        label="FactorAnalysis кросс-валидация: %d" % n_components_fa,
        linestyle="--",
    )
    plt.axvline(
        n_components_pca_mle,
        color="k",
        label="PCA MLE: %d" % n_components_pca_mle,
        linestyle="--",
    )

    # сравнить с другими ковариационными оценщиками
    plt.axhline(
        shrunk_cov_score(X),
        color="фиолетовый",
        label="Сжатое ковариационное MLE",
        linestyle="-.",
    )
    plt.axhline(
        lw_score(X),
        color="оранжевый",
        label="LedoitWolf MLE" % n_components_pca_mle,
        linestyle="-.",
    )

    plt.xlabel("количество компонентов")
    plt.ylabel("Оценки кросс-валидации")
    plt.legend(loc="нижний правый")
    plt.title(title)

plt.show()
```
