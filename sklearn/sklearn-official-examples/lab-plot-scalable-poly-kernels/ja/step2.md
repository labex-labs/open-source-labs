# ベースラインモデルの構築

ベースラインモデルを構築し、その精度を表示するために、元の特徴で線形 SVM を訓練します。

```python
from sklearn.svm import LinearSVC

# 元の特徴で線形 SVM を訓練
lsvm = LinearSVC(dual="auto")
lsvm.fit(X_train, y_train)
lsvm_score = 100 * lsvm.score(X_test, y_test)

# ベースラインモデルの精度を表示
print(f"Linear SVM score on raw features: {lsvm_score:.2f}%")
```
