# Treinar um Regressor Ridge sem Validação Cruzada

Enquanto `TargetEncoder.fit_transform` utiliza validação cruzada por intervalos, `TargetEncoder.transform` em si não executa nenhuma validação cruzada. Ele utiliza a agregação de todo o conjunto de treinamento para transformar as características categóricas. Portanto, podemos usar `TargetEncoder.fit` seguido de `TargetEncoder.transform` para desabilitar a validação cruzada. Esta codificação é então passada para o modelo Ridge. Execute o código a seguir para treinar o modelo Ridge sem validação cruzada:

```python
target_encoder = TargetEncoder(random_state=0)
target_encoder.fit(X_train, y_train)
X_train_no_cv_encoding = target_encoder.transform(X_train)
X_test_no_cv_encoding = target_encoder.transform(X_test)

model_no_cv = ridge.fit(X_train_no_cv_encoding, y_train)
print(
    "Model without CV on training set: ",
    model_no_cv.score(X_train_no_cv_encoding, y_train),
)
print(
    "Model without CV on test set: ", model_no_cv.score(X_test_no_cv_encoding, y_test)
)
```
