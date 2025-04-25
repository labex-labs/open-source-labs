# 特徴量の離散化を実装する

このステップでは、scikit - learn の KBinsDiscretizer クラスを使って、データセットに対して特徴量の離散化を実装します。これは、ビンのセットを作成することで特徴量を離散化し、次に離散値を one - hot エンコードします。その後、データを線形分類器に適合させ、性能を評価します。

```python
# 分類器を反復処理
for est_idx, (name, (estimator, param_grid)) in enumerate(zip(names, classifiers)):
    ax = axes[ds_cnt, est_idx + 1]

    clf = GridSearchCV(estimator=estimator, param_grid=param_grid)
    with ignore_warnings(category=ConvergenceWarning):
        clf.fit(X_train, y_train)
    score = clf.score(X_test, y_test)
    print(f"{name}: {score:.2f}")

    # 決定境界をプロットします。そのために、メッシュ [x_min, x_max]*[y_min, y_max] 内の各点に色を割り当てます。
    if hasattr(clf, "decision_function"):
        Z = clf.decision_function(np.column_stack([xx.ravel(), yy.ravel()]))
    else:
        Z = clf.predict_proba(np.column_stack([xx.ravel(), yy.ravel()]))[:, 1]

    # 結果をカラープロットに入れます
    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, cmap=cm_piyg, alpha=0.8)

    # 学習用のポイントをプロット
    ax.scatter(
        X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright, edgecolors="k"
    )
    # そしてテスト用のポイントをプロット
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
