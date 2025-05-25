# 데이터 시각화

이 단계에서는 특징 이산화 전에 합성 분류 데이터 세트를 시각화합니다. 각 데이터 세트에 대한 학습 및 테스트 데이터 포인트를 플롯합니다.

```python
fig, axes = plt.subplots(
    nrows=len(datasets), ncols=len(classifiers) + 1, figsize=(21, 9)
)

cm_piyg = plt.cm.PiYG
cm_bright = ListedColormap(["#b30065", "#178000"])

# 데이터 세트 반복
for ds_cnt, (X, y) in enumerate(datasets):
    print(f"\ndataset {ds_cnt}\n---------")

    # 학습 및 테스트 부분으로 분할
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.5, random_state=42
    )

    # 배경색을 위한 그리드 생성
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    # 먼저 데이터 세트를 플롯합니다.
    ax = axes[ds_cnt, 0]
    if ds_cnt == 0:
        ax.set_title("입력 데이터")
    # 학습 데이터 포인트를 플롯합니다.
    ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright, edgecolors="k")
    # 그리고 테스트 데이터 포인트를 플롯합니다.
    ax.scatter(
        X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright, alpha=0.6, edgecolors="k"
    )
    ax.set_xlim(xx.min(), xx.max())
    ax.set_ylim(yy.min(), yy.max())
    ax.set_xticks(())
    ax.set_yticks(())
```
