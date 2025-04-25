# モデルの適合

確率的主成分分析（Probabilistic PCA）と因子分析（Factor Analysis）のモデルをデータセットに適合させ、交差検証を使ってそれらの性能を評価します。また、シュリンク共分散推定器のスコアを計算し、結果を比較します。

```python
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA, FactorAnalysis
from sklearn.covariance import ShrunkCovariance, LedoitWolf
from sklearn.model_selection import cross_val_score, GridSearchCV

n_components = np.arange(0, n_features, 5)  # n_components のオプション

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

for X, title in [(X_homo, "同分散ノイズ"), (X_hetero, "異分散ノイズ")]:
    pca_scores, fa_scores = compute_scores(X)
    n_components_pca = n_components[np.argmax(pca_scores)]
    n_components_fa = n_components[np.argmax(fa_scores)]

    pca = PCA(svd_solver="full", n_components="mle")
    pca.fit(X)
    n_components_pca_mle = pca.n_components_

    print("PCA CV による最適な n_components = %d" % n_components_pca)
    print("FactorAnalysis CV による最適な n_components = %d" % n_components_fa)
    print("PCA MLE による最適な n_components = %d" % n_components_pca_mle)

    plt.figure()
    plt.plot(n_components, pca_scores, "b", label="PCA スコア")
    plt.plot(n_components, fa_scores, "r", label="FA スコア")
    plt.axvline(rank, color="g", label="真値：%d" % rank, linestyle="-")
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

    # 他の共分散推定器と比較
    plt.axhline(
        shrunk_cov_score(X),
        color="violet",
        label="シュリンク共分散 MLE",
        linestyle="-.",
    )
    plt.axhline(
        lw_score(X),
        color="orange",
        label="LedoitWolf MLE" % n_components_pca_mle,
        linestyle="-.",
    )

    plt.xlabel("成分数")
    plt.ylabel("CV スコア")
    plt.legend(loc="lower right")
    plt.title(title)

plt.show()
```
