# Создание базовой модели

Мы обучим линейный SVM на исходных признаках, чтобы создать базовую модель, и выведем ее точность.

```python
from sklearn.svm import LinearSVC

# Обучаем линейный SVM на исходных признаках
lsvm = LinearSVC(dual="auto")
lsvm.fit(X_train, y_train)
lsvm_score = 100 * lsvm.score(X_test, y_test)

# Выводим точность базовой модели
print(f"Linear SVM score on raw features: {lsvm_score:.2f}%")
```
