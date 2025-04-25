# 绘制精确率 - 召回率曲线

为了绘制精确率 - 召回率曲线，我们将使用 `sklearn.metrics` 库中的 `PrecisionRecallDisplay` 类。我们可以使用 `from_estimator` 或 `from_predictions` 方法来计算曲线。`from_estimator` 方法在绘制曲线之前为我们计算预测结果，而 `from_predictions` 方法则要求我们提供预测分数。

```python
from sklearn.metrics import PrecisionRecallDisplay

# 使用 from_estimator 方法
display = PrecisionRecallDisplay.from_estimator(
    classifier, X_test, y_test, name="LinearSVC", plot_chance_level=True
)
_ = display.ax_.set_title("2 类精确率 - 召回率曲线")

# 使用 from_predictions 方法
y_score = classifier.decision_function(X_test)

display = PrecisionRecallDisplay.from_predictions(
    y_test, y_score, name="LinearSVC", plot_chance_level=True
)
_ = display.ax_.set_title("2 类精确率 - 召回率曲线")
```
