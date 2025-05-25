# Treinar um Classificador Floresta Aleatória

Primeiro, carregamos o conjunto de dados de câncer de mama de Wisconsin e o dividimos em conjuntos de treinamento e teste. Em seguida, treinamos um Classificador Floresta Aleatória no conjunto de treinamento e avaliamos sua precisão no conjunto de teste.

```python
data = load_breast_cancer()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
print("Precisão nos dados de teste: {:.2f}".format(clf.score(X_test, y_test)))
```
