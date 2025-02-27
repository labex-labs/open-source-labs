# Ein Baselinemodell etablieren

Wir werden einen linearen SVM auf den ursprünglichen Merkmalen trainieren, um ein Baselinemodell zu etablieren und seine Genauigkeit auszugeben.

```python
from sklearn.svm import LinearSVC

# Trainiere einen linearen SVM auf den ursprünglichen Merkmalen
lsvm = LinearSVC(dual="auto")
lsvm.fit(X_train, y_train)
lsvm_score = 100 * lsvm.score(X_test, y_test)

# Gib die Genauigkeit des Baselinemodells aus
print(f"Linear SVM score on raw features: {lsvm_score:.2f}%")
```
