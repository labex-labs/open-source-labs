# 특징 이산화 구현

이 단계에서는 scikit-learn 의 `KBinsDiscretizer` 클래스를 사용하여 데이터 세트에 특징 이산화를 구현합니다. 이는 특징을 일련의 구간으로 나누고 이산화된 값을 원 - 핫 인코딩하여 특징을 이산화합니다. 그런 다음 데이터를 선형 분류기에 맞추고 성능을 평가합니다.

```python
# 분류기 반복
for est_idx, (name, (estimator, param_grid)) in enumerate(zip(names, classifiers)):
    ax = axes[ds_cnt, est_idx + 1]

    clf = GridSearchCV(estimator=estimator, param_grid=param_grid)
    with ignore_warnings(category=ConvergenceWarning):
        clf.fit(X_train, y_train)
    score = clf.score(X_test, y_test)
    print(f"{name}: {score:.2f}")

    # 결정 경계를 플롯합니다. 이를 위해 메쉬 [x_min, x_max] * [y_min, y_max] 의 각 점에 색상을 할당합니다.
    if hasattr(clf, "decision_function"):
        Z = clf.decision_function(np.column_stack([xx.ravel(), yy.ravel()]))
    else:
        Z = clf.predict_proba(np.column_stack([xx.ravel(), yy.ravel()]))[:, 1]

    # 결과를 색상 플롯에 넣습니다.
    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, cmap=cm_piyg, alpha=0.8)

    # 학습 데이터 포인트를 플롯합니다.
    ax.scatter(
        X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright, edgecolors="k"
    )
    # 그리고 테스트 데이터 포인트를 플롯합니다.
    ax.scatter(
        X_test[:, 0],
        X_test[:, 1],
        c=y_test,
        cmap=cm_bright,
        edgecolors="k",
        alpha=0.6,
    )
    ax.set_xlim(xx.min(), xx.max())
    ax.set_ylim(yy.min(), yy.max())
    ax.set_xticks(())
    ax.set_yticks(())

    if ds_cnt == 0:
        ax.set_title(name.replace(" + ", "\n"))
    ax.text(
        0.95,
        0.06,
        (f"{score:.2f}").lstrip("0"),
        size=15,
        bbox=dict(boxstyle="round", alpha=0.8, facecolor="white"),
        transform=ax.transAxes,
        horizontalalignment="right",
    )
```
