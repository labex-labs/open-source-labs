# Настроить модель SVM

Далее мы настроим модель SVM на наш набор данных с использованием линейного ядра и параметра регуляризации 1000. Мы будем использовать функцию `svm.SVC()` из scikit-learn для создания классификатора SVM.

```python
from sklearn import svm

# fit the SVM model
clf = svm.SVC(kernel="linear", C=1000)
clf.fit(X, y)
```
