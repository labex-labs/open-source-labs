# Feature-Diskretisierung implementieren

In diesem Schritt werden wir die Feature-Diskretisierung auf den Datensätzen mit der KBinsDiscretizer-Klasse aus scikit-learn implementieren. Dies wird die Features diskretisieren, indem ein Satz von Bins erstellt und dann die diskreten Werte mit One-Hot-Codierung codiert werden. Anschließend werden die Daten an einen linearen Klassifizierer angepasst und die Leistung ausgewertet.

```python
# iterieren über die Klassifizierer
for est_idx, (name, (estimator, param_grid)) in enumerate(zip(names, classifiers)):
    ax = axes[ds_cnt, est_idx + 1]

    clf = GridSearchCV(estimator=estimator, param_grid=param_grid)
    mit ignore_warnings(category=ConvergenceWarning):
        clf.fit(X_train, y_train)
    score = clf.score(X_test, y_test)
    print(f"{name}: {score:.2f}")

    # plotten Sie die Entscheidungsgrenze. Dazu werden wir jeder
    # Punkt im Gitter [x_min, x_max]*[y_min, y_max] eine Farbe zuweisen.
    wenn hasattr(clf, "decision_function"):
        Z = clf.decision_function(np.column_stack([xx.ravel(), yy.ravel()]))
    sonst:
        Z = clf.predict_proba(np.column_stack([xx.ravel(), yy.ravel()]))[:, 1]

    # bringen Sie das Ergebnis in einen Farbplot
    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, cmap=cm_piyg, alpha=0.8)

    # plotten Sie die Trainingspunkte
    ax.scatter(
        X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright, edgecolors="k"
    )
    # und Testpunkte
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

    wenn ds_cnt == 0:
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
