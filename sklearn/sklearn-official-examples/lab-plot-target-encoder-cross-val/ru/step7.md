# Обучение регрессора Ridge без кросс-валидации

В то время как `TargetEncoder.fit_transform` использует интервальную кросс-валидацию, сам метод `TargetEncoder.transform` не выполняет никакой кросс-валидации. Он использует агрегацию всего обучающего набора данных для преобразования категориальных признаков. Таким образом, мы можем использовать `TargetEncoder.fit` с последующим вызовом `TargetEncoder.transform` для отключения кросс-валидации. Затем это закодированное представление передается модели Ridge. Выполните следующий код для обучения модели Ridge без кросс-валидации:

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
