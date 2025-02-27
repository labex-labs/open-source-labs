# Построение кривой Точность - Полнота

Для построения кривой Точность - Полнота мы будем использовать класс PrecisionRecallDisplay из библиотеки sklearn.metrics. Мы можем использовать метод from_estimator или from_predictions для вычисления кривой. Метод from_estimator вычисляет предсказания для нас перед построением кривой, в то время как метод from_predictions требует от нас предоставить предсказанные оценки.

```python
from sklearn.metrics import PrecisionRecallDisplay

# Использование метода from_estimator
display = PrecisionRecallDisplay.from_estimator(
    classifier, X_test, y_test, name="LinearSVC", plot_chance_level=True
)
_ = display.ax_.set_title("2-class Precision-Recall curve")

# Использование метода from_predictions
y_score = classifier.decision_function(X_test)

display = PrecisionRecallDisplay.from_predictions(
    y_test, y_score, name="LinearSVC", plot_chance_level=True
)
_ = display.ax_.set_title("2-class Precision-Recall curve")
```
