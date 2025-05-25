# Auto-treinamento com Limiares Variáveis

```python
for i, threshold in enumerate(x_values):
    self_training_clf = SelfTrainingClassifier(base_classifier, threshold=threshold)

    skfolds = StratifiedKFold(n_splits=n_splits)
    for fold, (train_index, test_index) in enumerate(skfolds.split(X, y)):
        X_train = X[train_index]
        y_train = y[train_index]
        X_test = X[test_index]
        y_test = y[test_index]
        y_test_true = y_true[test_index]

        self_training_clf.fit(X_train, y_train)

        amount_labeled[i, fold] = (
            total_samples
            - np.unique(self_training_clf.labeled_iter_, return_counts=True)[1][0]
        )

        amount_iterations[i, fold] = np.max(self_training_clf.labeled_iter_)

        y_pred = self_training_clf.predict(X_test)
        scores[i, fold] = accuracy_score(y_test_true, y_pred)
```

Realizamos auto-treinamento com diferentes limiares, utilizando o nosso classificador base e a classe `SelfTrainingClassifier` do scikit-learn. Usamos validação cruzada estratificada k-fold para dividir os nossos dados em conjuntos de treino e teste. Em seguida, ajustamos o classificador de auto-treinamento no conjunto de treino e calculamos a precisão do classificador no conjunto de teste. Também armazenamos a quantidade de amostras rotuladas e o número de iteração para cada dobra.
