# Implement Feature Discretization

In this step, we will implement feature discretization on the datasets using the KBinsDiscretizer class from scikit-learn. This will discretize the features by creating a set of bins and then one-hot encoding the discrete values. We will then fit the data to a linear classifier and evaluate the performance.

```python
# iterate over classifiers
for est_idx, (name, (estimator, param_grid)) in enumerate(zip(names, classifiers)):
    ax = axes[ds_cnt, est_idx + 1]

    clf = GridSearchCV(estimator=estimator, param_grid=param_grid)
    with ignore_warnings(category=ConvergenceWarning):
        clf.fit(X_train, y_train)
    score = clf.score(X_test, y_test)
    print(f"{name}: {score:.2f}")

    # plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]*[y_min, y_max].
    if hasattr(clf, "decision_function"):
        Z = clf.decision_function(np.column_stack([xx.ravel(), yy.ravel()]))
    else:
        Z = clf.predict_proba(np.column_stack([xx.ravel(), yy.ravel()]))[:, 1]

    # put the result into a color plot
    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, cmap=cm_piyg, alpha=0.8)

    # plot the training points
    ax.scatter(
        X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright, edgecolors="k"
    )
    # and testing points
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
