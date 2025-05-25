# 분류기 적합 및 결정 경계 시각화

각 분류기를 각 데이터셋에 적용하고 결정 경계를 시각화합니다. `contourf`를 사용하여 결정 경계를 그리고 `scatter`를 사용하여 학습 및 테스트 데이터 포인트를 시각화합니다. 각 플롯에 정확도 점수도 표시합니다.

```python
    # 분류기 반복
    for name, clf in zip(names, classifiers):
        ax = plt.subplot(len(datasets), len(classifiers) + 1, i)
        clf.fit(X_train, y_train)
        score = clf.score(X_test, y_test)

        # 결정 경계를 플롯합니다. 이를 위해 [x_min, x_max] x [y_min, y_max] 메쉬의 각 점에 색상을 할당합니다.
        if hasattr(clf, "decision_function"):
            Z = clf.decision_function(np.column_stack([xx.ravel(), yy.ravel()]))
        else:
            Z = clf.predict_proba(np.column_stack([xx.ravel(), yy.ravel()]))[:, 1]

        # 결과를 색상 플롯으로 표시
        Z = Z.reshape(xx.shape)
        ax.contourf(xx, yy, Z, cmap=cm, alpha=0.8)

        # 학습 데이터 포인트도 플롯합니다.
        ax.scatter(
            X_train[:, 0],
            X_train[:, 1],
            c=y_train,
            cmap=cm_bright,
            edgecolors="black",
            s=25,
        )
        # 그리고 테스트 데이터 포인트를 플롯합니다.
        ax.scatter(
            X_test[:, 0],
            X_test[:, 1],
            c=y_test,
            cmap=cm_bright,
            alpha=0.6,
            edgecolors="black",
            s=25,
        )

        ax.set_xlim(xx.min(), xx.max())
        ax.set_ylim(yy.min(), yy.max())
        ax.set_xticks(())
        ax.set_yticks(())
        ax.set_title(name)
        ax.text(
            xx.max() - 0.3,
            yy.min() + 0.3,
            f"{score:.3f}".lstrip("0"),
            size=15,
            horizontalalignment="right",
        )
        i += 1
```
