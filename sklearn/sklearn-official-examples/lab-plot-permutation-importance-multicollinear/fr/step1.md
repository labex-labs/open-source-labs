# Entraîner un classifieur Random Forest

Nous commençons par charger l'ensemble de données du cancer du sein du Wisconsin et le divisons en ensembles d'entraînement et de test. Nous entraînons ensuite un classifieur Random Forest sur l'ensemble d'entraînement et évaluons sa précision sur l'ensemble de test.

```python
data = load_breast_cancer()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
print("Accuracy on test data: {:.2f}".format(clf.score(X_test, y_test)))
```
