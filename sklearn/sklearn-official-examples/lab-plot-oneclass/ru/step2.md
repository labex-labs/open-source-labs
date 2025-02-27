# Настраиваем модель одноклассовой SVM

Далее мы настроим модель одноклассовой SVM на сгенерированных данных.

```python
# Настраиваем модель
clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
clf.fit(X_train)

# Предсказываем метки для обучающих данных, обычных новаторских наблюдений и аномальных новаторских наблюдений
y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)
```
