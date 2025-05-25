# 서로 다른 커널을 사용한 모델 학습

이제 선형, rbf, poly 세 가지 서로 다른 커널을 사용하여 SVM 모델을 학습시키겠습니다. 각 커널에 대해 훈련 데이터에 모델을 맞추고, 결정 경계를 플롯하고, 테스트 데이터의 정확도를 보여줍니다.

```python
# 모델 학습
for kernel in ("linear", "rbf", "poly"):
    clf = svm.SVC(kernel=kernel, gamma=10)
    clf.fit(X_train, y_train)

    plt.figure()
    plt.clf()
    plt.scatter(
        X[:, 0], X[:, 1], c=y, zorder=10, cmap=plt.cm.Paired, edgecolor="k", s=20
    )

    # 테스트 데이터를 원으로 표시
    plt.scatter(
        X_test[:, 0], X_test[:, 1], s=80, facecolors="none", zorder=10, edgecolor="k"
    )

    plt.axis("tight")
    x_min = X[:, 0].min()
    x_max = X[:, 0].max()
    y_min = X[:, 1].min()
    y_max = X[:, 1].max()

    XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
    Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()])

    # 결과를 색상 플롯으로 표시
    Z = Z.reshape(XX.shape)
    plt.pcolormesh(XX, YY, Z > 0, cmap=plt.cm.Paired)
    plt.contour(
        XX,
        YY,
        Z,
        colors=["k", "k", "k"],
        linestyles=["--", "-", "--"],
        levels=[-0.5, 0, 0.5],
    )

    plt.title(kernel)
    plt.show()

    print(f"Accuracy with {kernel} kernel: {clf.score(X_test, y_test)}")
```
