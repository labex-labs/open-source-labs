# 拟合模型

我们将把概率主成分分析（Probabilistic PCA）和因子分析（Factor Analysis）模型拟合到数据集上，并使用交叉验证来评估它们的性能。我们还将计算收缩协方差估计器的分数，并比较结果。

```python
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA, FactorAnalysis
from sklearn.covariance import ShrunkCovariance, LedoitWolf
from sklearn.model_selection import cross_val_score, GridSearchCV

n_components = np.arange(0, n_features, 5)  # n_components 的选项

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

for X, title in [(X_homo, "同方差噪声"), (X_hetero, "异方差噪声")]:
    pca_scores, fa_scores = compute_scores(X)
    n_components_pca = n_components[np.argmax(pca_scores)]
    n_components_fa = n_components[np.argmax(fa_scores)]

    pca = PCA(svd_solver="full", n_components="mle")
    pca.fit(X)
    n_components_pca_mle = pca.n_components_

    print("通过 PCA 交叉验证得到的最佳 n_components = %d" % n_components_pca)
    print("通过因子分析交叉验证得到的最佳 n_components = %d" % n_components_fa)
    print("通过 PCA 最大似然估计得到的最佳 n_components = %d" % n_components_pca_mle)

    plt.figure()
    plt.plot(n_components, pca_scores, "b", label="PCA 分数")
    plt.plot(n_components, fa_scores, "r", label="因子分析分数")
    plt.axvline(rank, color="g", label="真实值：%d" % rank, linestyle="-")
    plt.axvline(
        n_components_pca,
        color="b",
        label="PCA 交叉验证：%d" % n_components_pca,
        linestyle="--"
    )
    plt.axvline(
        n_components_fa,
        color="r",
        label="因子分析交叉验证：%d" % n_components_fa,
        linestyle="--"
    )
    plt.axvline(
        n_components_pca_mle,
        color="k",
        label="PCA 最大似然估计：%d" % n_components_pca_mle,
        linestyle="--"
    )

    # 与其他协方差估计器比较
    plt.axhline(
        shrunk_cov_score(X),
        color="violet",
        label="收缩协方差最大似然估计",
        linestyle="-."
    )
    plt.axhline(
        lw_score(X),
        color="orange",
        label="LedoitWolf 最大似然估计 %d" % n_components_pca_mle,
        linestyle="-."
    )

    plt.xlabel("成分数量")
    plt.ylabel("交叉验证分数")
    plt.legend(loc="lower right")
    plt.title(title)

plt.show()
```
