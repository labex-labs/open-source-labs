# カーネル化 SVM モデルの構築

カーネルの性能をどの程度近似できるかを見るために、カーネル化 SVM を訓練します。

```python
from sklearn.svm import SVC

# カーネル化 SVM を訓練
ksvm = SVC(C=500.0, kernel="poly", degree=4, coef0=0, gamma=1.0)
ksvm.fit(X_train, y_train)
ksvm_score = 100 * ksvm.score(X_test, y_test)

# カーネル化 SVM の精度を表示
print(f"Kernel-SVM score on raw features: {ksvm_score:.2f}%")
```
