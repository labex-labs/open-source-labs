# 混同行列の生成

scikit-learnのConfusionMatrixDisplayクラスを使用して混同行列を生成します。混同行列は、各クラスに対する正解予測と不正解予測の数を示します。

```python
np.set_printoptions(precision=2)
disp = ConfusionMatrixDisplay.from_estimator(
    classifier,
    X_test,
    y_test,
    display_labels=class_names,
    cmap=plt.cm.Blues,
    normalize=None,
)
```
