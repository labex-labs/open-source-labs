# Ordinary Least Squares

> Wenn Sie keine Vorkenntnisse in Machine Learning haben, starten Sie sich mit [Supervised Learning: Regression](https://labex.io/courses/supervised-learning-regression) ein.

Ordinary Least Squares (OLS) ist eine lineare Regressionsmethode, die die Summe der quadrierten Differenzen zwischen den beobachteten Zielwerten und den vorhergesagten Zielwerten minimiert. Mathematisch löst es ein Problem der Form:
$$\min_{w} || X w - y||_2^2$$

Lassen Sie uns beginnen, ein lineares Regressionsmodell mit OLS anzupassen.

```python
from sklearn import linear_model

reg = linear_model.LinearRegression()
X = [[0, 0], [1, 1], [2, 2]]
y = [0, 1, 2]
reg.fit(X, y)

print(reg.coef_)
```

- Wir importieren das Modul `linear_model` aus scikit-learn.
- Wir erstellen eine Instanz von `LinearRegression`.
- Wir verwenden die `fit`-Methode, um das Modell an die Trainingsdaten anzupassen.
- Wir drucken die Koeffizienten des linearen Modells.
