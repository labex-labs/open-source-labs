# Precision-Recall曲線を描画する

Precision-Recall曲線を描画するには、sklearn.metricsライブラリのPrecisionRecallDisplayクラスを使用します。曲線を計算するには、from_estimatorまたはfrom_predictionsメソッドのどちらかを使用できます。from_estimatorメソッドは、曲線を描画する前に予測を計算しますが、from_predictionsメソッドは予測スコアを提供する必要があります。

```python
from sklearn.metrics import PrecisionRecallDisplay

# from_estimatorメソッドを使用
display = PrecisionRecallDisplay.from_estimator(
    classifier, X_test, y_test, name="LinearSVC", plot_chance_level=True
)
_ = display.ax_.set_title("2-class Precision-Recall curve")

# from_predictionsメソッドを使用
y_score = classifier.decision_function(X_test)

display = PrecisionRecallDisplay.from_predictions(
    y_test, y_score, name="LinearSVC", plot_chance_level=True
)
_ = display.ax_.set_title("2-class Precision-Recall curve")
```
