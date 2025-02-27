# Обучение支持向量机 (support vector machine)

Мы обучим классификатор на основе支持向量机 (support vector machine) на обучающих примерах с использованием метода `svm.SVC()` из `sklearn`.

```python
clf = svm.SVC(gamma=0.001)
clf.fit(X_train, y_train)
```
