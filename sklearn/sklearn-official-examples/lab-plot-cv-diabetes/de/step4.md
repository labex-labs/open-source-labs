# Verwenden von LassoCV, um die Alpha-Auswahl zu überprüfen

Schließlich werden wir LassoCV verwenden, um zu sehen, wie vertrauenswürdig die Auswahl von Alpha ist. Wir werden KFold mit 3 Folds verwenden.

```python
from sklearn.linear_model import LassoCV
from sklearn.model_selection import KFold

lasso_cv = LassoCV(alphas=alphas, random_state=0, max_iter=10000)
k_fold = KFold(3)

print("Antwort auf die Bonus-Frage:", "wie vertrauenswürdig ist die Auswahl von Alpha?")
print()
print("Alpha-Parameter, die die Verallgemeinerungsscore auf verschiedenen")
print("Teilmengen der Daten maximieren:")
for k, (train, test) in enumerate(k_fold.split(X, y)):
    lasso_cv.fit(X[train], y[train])
    print(
        "[Fold {0}] alpha: {1:.5f}, score: {2:.5f}".format(
            k, lasso_cv.alpha_, lasso_cv.score(X[test], y[test])
        )
    )

print()
print("Antwort: Nicht sehr, da wir für verschiedene Teilmengen der Daten unterschiedliche Alphas erhalten haben und darüber hinaus die Scores für diese Alphas sich erheblich unterscheiden.")
```
