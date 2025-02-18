# モデルの定義

ガウシアンカーネル（radial basis function kernel）を持つサポートベクター分類器（Support Vector Classifier）を使用します。

```python
from sklearn.svm import SVC

# We will use a Support Vector Classifier with "rbf" kernel
svm = SVC(kernel="rbf")
```
