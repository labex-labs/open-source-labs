# 모델 적합

확률적 PCA 및 요인 분석 모델을 데이터셋에 적합하고, 교차 검증을 사용하여 성능을 평가할 것입니다. 또한 축소 공분산 추정량의 점수를 계산하고 결과를 비교할 것입니다.

```python
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA, FactorAnalysis
from sklearn.covariance import ShrunkCovariance, LedoitWolf
from sklearn.model_selection import cross_val_score, GridSearchCV

n_components = np.arange(0, n_features, 5)  # options for n_components

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

for X, title in [(X_homo, "동종 노이즈"), (X_hetero, "이종 노이즈")]:
    pca_scores, fa_scores = compute_scores(X)
    n_components_pca = n_components[np.argmax(pca_scores)]
    n_components_fa = n_components[np.argmax(fa_scores)]

    pca = PCA(svd_solver="full", n_components="mle")
    pca.fit(X)
    n_components_pca_mle = pca.n_components_

    print("PCA CV에 의한 최적 n_components = %d" % n_components_pca)
    print("FactorAnalysis CV에 의한 최적 n_components = %d" % n_components_fa)
    print("PCA MLE에 의한 최적 n_components = %d" % n_components_pca_mle)

    plt.figure()
    plt.plot(n_components, pca_scores, "b", label="PCA 점수")
    plt.plot(n_components, fa_scores, "r", label="FA 점수")
    plt.axvline(rank, color="g", label="진실값: %d" % rank, linestyle="-")
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

    # 다른 공분산 추정량과 비교
    plt.axhline(
        shrunk_cov_score(X),
        color="violet",
        label="축소 공분산 MLE",
        linestyle="-.",
    )
    plt.axhline(
        lw_score(X),
        color="orange",
        label="LedoitWolf MLE",
        linestyle="-.",
    )

    plt.xlabel("컴포넌트 수")
    plt.ylabel("교차 검증 점수")
    plt.legend(loc="lower right")
    plt.title(title)

plt.show()
```
