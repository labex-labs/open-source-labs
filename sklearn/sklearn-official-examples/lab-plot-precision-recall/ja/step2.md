# Precision-Recall 曲線を描画する

Precision-Recall 曲線を描画するには、sklearn.metrics ライブラリの PrecisionRecallDisplay クラスを使用します。曲線を計算するには、from_estimator または from_predictions メソッドのどちらかを使用できます。from_estimator メソッドは、曲線を描画する前に予測を計算しますが、from_predictions メソッドは予測スコアを提供する必要があります。

```python
from sklearn.metrics import PrecisionRecallDisplay

# from_estimator メソッドを使用
display = PrecisionRecallDisplay.from_estimator(
    classifier, X_test, y_test, name="LinearSVC", plot_chance_level=True
)
_ = display.ax_.set_title("2-class Precision-Recall curve")

# from_predictions メソッドを使用
y_score = classifier.decision_function(X_test)

display = PrecisionRecallDisplay.from_predictions(
    y_test, y_score, name="LinearSVC", plot_chance_level=True
)
_ = display.ax_.set_title("2-class Precision-Recall curve")
```
