# Построение границы решения модели многонаправленной логистической регрессии

Теперь мы построим поверхность решения модели многонаправленной логистической регрессии с использованием функции `DecisionBoundaryDisplay` из scikit-learn. Мы установим метод ответа в `"predict"`, палитру цветов в `"plt.cm.Paired"` и также построим точки обучения.

```python
_, ax = plt.subplots()
DecisionBoundaryDisplay.from_estimator(
        clf, X, response_method="predict", cmap=plt.cm.Paired, ax=ax
    )
plt.title("Decision surface of LogisticRegression (multinomial)")
plt.axis("tight")

colors = "bry"
for i, color in zip(clf.classes_, colors):
        idx = np.where(y == i)
        plt.scatter(
            X[idx, 0], X[idx, 1], c=color, cmap=plt.cm.Paired, edgecolor="black", s=20
        )
```
