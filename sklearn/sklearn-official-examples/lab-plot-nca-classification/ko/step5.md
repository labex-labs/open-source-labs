# 분류기 학습 및 테스트

이제 분류기를 학습하고 테스트합니다. 분류기 목록을 반복하여 학습 데이터에 맞춥니다. 그런 다음 클래스 결정 경계를 플롯하고 테스트 데이터에 대한 점수를 계산합니다.

```python
for name, clf in zip(names, classifiers):
    clf.fit(X_train, y_train)
    score = clf.score(X_test, y_test)

    _, ax = plt.subplots()
    DecisionBoundaryDisplay.from_estimator(
        clf,
        X,
        cmap=cmap_light,
        alpha=0.8,
        ax=ax,
        response_method="predict",
        plot_method="pcolormesh",
        shading="auto",
    )

    # 학습 및 테스트 데이터 포인트도 플롯
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, edgecolor="k", s=20)
    plt.title("{} (k = {})".format(name, n_neighbors))
    plt.text(
        0.9,
        0.1,
        "{:.2f}".format(score),
        size=15,
        ha="center",
        va="center",
        transform=plt.gca().transAxes,
    )

plt.show()
```
