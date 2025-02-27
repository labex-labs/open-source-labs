# Оценка

В этом шаге мы оцениваем производительность модели на тестовом наборе данных. Мы используем функцию `classification_report` из модуля `sklearn.metrics`, чтобы сгенерировать отчёт о классификации как для модели конвейера, так и для модели логистической регрессии.

```python
from sklearn import metrics

Y_pred = rbm_features_classifier.predict(X_test)
print(
    "Logistic regression using RBM features:\n%s\n"
    % (metrics.classification_report(Y_test, Y_pred))
)

# Training the Logistic regression classifier directly on the pixel
raw_pixel_classifier = clone(logistic)
raw_pixel_classifier.C = 100.0
raw_pixel_classifier.fit(X_train, Y_train)

Y_pred = raw_pixel_classifier.predict(X_test)
print(
    "Logistic regression using raw pixel features:\n%s\n"
    % (metrics.classification_report(Y_test, Y_pred))
)
```
