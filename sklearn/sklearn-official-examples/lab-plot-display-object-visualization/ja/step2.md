# ConfusionMatrixDisplay の作成

フィットさせたモデルを使って、テスト用データセットに対するモデルの予測を計算します。これらの予測値を使って混同行列を計算し、`ConfusionMatrixDisplay` でプロットします。

```python
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

y_pred = clf.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

cm_display = ConfusionMatrixDisplay(cm).plot()
```
