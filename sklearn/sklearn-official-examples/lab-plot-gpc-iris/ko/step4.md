# 예측 확률 시각화

이제 메쉬 상의 각 점에 대한 예측 확률을 시각화합니다. 등방성 RBF 커널과 이방성 RBF 커널에 대한 두 개의 서브플롯을 생성합니다. `predict_proba` 메서드를 사용하여 메쉬 상의 각 점에 대한 예측 확률을 얻습니다. 그런 다음 메쉬 상에 예측 확률을 색상 플롯으로 표시합니다. 또한 각 아이리스 꽃 종에 대한 학습 데이터 포인트를 플롯합니다.

```python
titles = ["Isotropic RBF", "Anisotropic RBF"]
plt.figure(figsize=(10, 5))
for i, clf in enumerate((gpc_rbf_isotropic, gpc_rbf_anisotropic)):
    # 예측 확률을 플롯합니다. 이를 위해 메쉬 [x_min, m_max]x[y_min, y_max] 의 각 점에 색상을 할당합니다.
    plt.subplot(1, 2, i + 1)

    Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])

    # 결과를 색상 플롯에 넣습니다.
    Z = Z.reshape((xx.shape[0], xx.shape[1], 3))
    plt.imshow(Z, extent=(x_min, x_max, y_min, y_max), origin="lower")

    # 학습 데이터 포인트도 플롯합니다.
    plt.scatter(X[:, 0], X[:, 1], c=np.array(["r", "g", "b"])[y], edgecolors=(0, 0, 0))
    plt.xlabel("꽃받침 길이")
    plt.ylabel("꽃받침 너비")
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.title(
        "%s, LML: %.3f" % (titles[i], clf.log_marginal_likelihood(clf.kernel_.theta))
    )

plt.tight_layout()
plt.show()
```
