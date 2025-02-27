# ROC 曲線と DET 曲線を描画する

それぞれ ROC 曲線と DET 曲線を描画するために、scikit-learn の `RocCurveDisplay` と `DetCurveDisplay` クラスを使用します。`RocCurveDisplay.from_estimator` 関数は ROC 曲線を計算し、与えられた軸に描画します。同様に、`DetCurveDisplay.from_estimator` 関数は DET 曲線を計算し、与えられた軸に描画します。2 つのサブプロットを作成し、1 つは ROC 曲線用で、もう 1 つは DET 曲線用で、各分類器の曲線を描画します。

```python
import matplotlib.pyplot as plt
from sklearn.metrics import DetCurveDisplay, RocCurveDisplay

fig, [ax_roc, ax_det] = plt.subplots(1, 2, figsize=(11, 5))

for name, clf in classifiers.items():
    clf.fit(X_train, y_train)

    RocCurveDisplay.from_estimator(clf, X_test, y_test, ax=ax_roc, name=name)
    DetCurveDisplay.from_estimator(clf, X_test, y_test, ax=ax_det, name=name)

ax_roc.set_title("Receiver Operating Characteristic (ROC) curves")
ax_det.set_title("Detection Error Tradeoff (DET) curves")

ax_roc.grid(linestyle="--")
ax_det.grid(linestyle="--")

plt.legend()
plt.show()
```
