# 정밀도 - 재현율 곡선 플롯

정밀도 - 재현율 곡선을 플롯하려면 `sklearn.metrics` 라이브러리의 `PrecisionRecallDisplay` 클래스를 사용합니다. 곡선을 계산하기 위해 `from_estimator` 또는 `from_predictions` 메서드를 사용할 수 있습니다. `from_estimator` 메서드는 곡선을 플롯하기 전에 예측을 계산하는 반면, `from_predictions` 메서드는 예측 점수를 직접 제공해야 합니다.

```python
from sklearn.metrics import PrecisionRecallDisplay

# from_estimator 메서드 사용
display = PrecisionRecallDisplay.from_estimator(
    classifier, X_test, y_test, name="LinearSVC", plot_chance_level=True
)
_ = display.ax_.set_title("2-class 정밀도 - 재현율 곡선")

# from_predictions 메서드 사용
y_score = classifier.decision_function(X_test)

display = PrecisionRecallDisplay.from_predictions(
    y_test, y_score, name="LinearSVC", plot_chance_level=True
)
_ = display.ax_.set_title("2-class 정밀도 - 재현율 곡선")
```
