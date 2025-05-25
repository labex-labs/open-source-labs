# 결정 경계 시각화

이 단계에서는 정의된 모델의 결정 경계를 아이리스 데이터셋에 시각화합니다.

```python
plot_idx = 1

for pair in ([0, 1], [0, 2], [2, 3]):
    for model in models:
        # 해당하는 두 개의 특징만 사용
        X = iris.data[:, pair]
        y = iris.target

        # 셔플
        idx = np.arange(X.shape[0])
        np.random.seed(RANDOM_SEED)
        np.random.shuffle(idx)
        X = X[idx]
        y = y[idx]

        # 표준화
        mean = X.mean(axis=0)
        std = X.std(axis=0)
        X = (X - mean) / std

        # 학습
        model.fit(X, y)

        scores = model.score(X, y)
        # 각 열과 콘솔에 대한 제목을 str() 을 사용하여 만들고
        # 문자열의 불필요한 부분을 잘라냅니다.
        model_title = str(type(model)).split(".")[-1][:-2][: -len("Classifier")]

        model_details = model_title
        if hasattr(model, "estimators_"):
            model_details += " with {} estimators".format(len(model.estimators_))
        print(model_details + " with features", pair, "has a score of", scores)

        plt.subplot(3, 4, plot_idx)
        if plot_idx <= len(models):
            # 각 열 위에 제목 추가
            plt.title(model_title, fontsize=9)

        # 결정 경계를 미세한 메쉬를 입력으로 사용하여 채워진 등고선 플롯을 사용하여 플롯
        x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx, yy = np.meshgrid(
            np.arange(x_min, x_max, plot_step), np.arange(y_min, y_max, plot_step)
        )

        # 단일 DecisionTreeClassifier 를 플롯하거나, 분류기 앙상블의 결정 경계를 알파 블렌딩
        if isinstance(model, DecisionTreeClassifier):
            Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
            Z = Z.reshape(xx.shape)
            cs = plt.contourf(xx, yy, Z, cmap=cmap)
        else:
            # 사용 중인 추정기의 수에 따라 알파 블렌딩 수준 선택
            # (AdaBoost 는 초기 단계에서 충분히 좋은 적합을 달성하면 최대 추정기보다 적은 추정기를 사용할 수 있음)
            estimator_alpha = 1.0 / len(model.estimators_)
            for tree in model.estimators_:
                Z = tree.predict(np.c_[xx.ravel(), yy.ravel()])
                Z = Z.reshape(xx.shape)
                cs = plt.contourf(xx, yy, Z, alpha=estimator_alpha, cmap=cmap)

        # 앙상블 분류의 집합을 플롯하기 위해 더 거친 그리드를 만듭니다.
        # 이 점들은 정기적으로 배치되고 검은색 윤곽선이 없습니다.
        xx_coarser, yy_coarser = np.meshgrid(
            np.arange(x_min, x_max, plot_step_coarser),
            np.arange(y_min, y_max, plot_step_coarser),
        )
        Z_points_coarser = model.predict(
            np.c_[xx_coarser.ravel(), yy_coarser.ravel()]
        ).reshape(xx_coarser.shape)
        cs_points = plt.scatter(
            xx_coarser,
            yy_coarser,
            s=15,
            c=Z_points_coarser,
            cmap=cmap,
            edgecolors="none",
        )

        # 학습 데이터 포인트를 플롯합니다. 이들은 클러스터링되어 검은색 윤곽선이 있습니다.
        plt.scatter(
            X[:, 0],
            X[:, 1],
            c=y,
            cmap=ListedColormap(["r", "y", "b"]),
            edgecolor="k",
            s=20,
        )
        plot_idx += 1  # 다음 플롯으로 이동

plt.suptitle("아이리스 데이터셋의 특징 부분 집합에 대한 분류기", fontsize=12)
plt.axis("tight")
plt.tight_layout(h_pad=0.2, w_pad=0.2, pad=2.5)
plt.show()
```
