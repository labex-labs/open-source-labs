# サポートベクターマシン（SVM）モデルの作成

次に、線形カーネルを持つ SVM モデルを作成します。

```python
from sklearn import svm

svc = svm.SVC(kernel="linear")
```
