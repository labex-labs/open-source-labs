# 결정 경계 시각화

두 가지 다른 가중치 값 ("균일" 및 "거리") 을 반복하여 각 가중치 값에 대한 결정 경계를 플롯합니다. 분류를 위해 `neighbors` 모듈의 `KNeighborsClassifier` 클래스를 사용합니다.

```python
n_neighbors = 15

for weights in ["uniform", "distance"]:
    # Neighbours Classifier 의 인스턴스를 생성하고 데이터를 맞춥니다.
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X, y)

    # 결정 경계를 플롯합니다.
    _, ax = plt.subplots()
    DecisionBoundaryDisplay.from_estimator(
        clf,
        X,
        cmap=cmap_light,
        ax=ax,
        response_method="predict",
        plot_method="pcolormesh",
        xlabel=iris.feature_names[0],
        ylabel=iris.feature_names[1],
        shading="auto",
    )

    # 학습 데이터 포인트를 플롯합니다.
    sns.scatterplot(
        x=X[:, 0],
        y=X[:, 1],
        hue=iris.target_names[y],
        palette=cmap_bold,
        alpha=1.0,
        edgecolor="black",
    )
    plt.title(
        "3-클래스 분류 (k = %i, 가중치 = '%s')" % (n_neighbors, weights)
    )

plt.show()
```
