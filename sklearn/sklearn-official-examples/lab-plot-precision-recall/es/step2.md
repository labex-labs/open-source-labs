# Trazar la curva Precision-Recall

Para trazar la curva Precision-Recall, utilizaremos la clase PrecisionRecallDisplay de la biblioteca sklearn.metrics. Podemos utilizar el método from_estimator o from_predictions para calcular la curva. El método from_estimator calcula las predicciones para nosotros antes de trazar la curva, mientras que el método from_predictions requiere que nosotros proporcionemos las puntuaciones predichas.

```python
from sklearn.metrics import PrecisionRecallDisplay

# Utilizando el método from_estimator
display = PrecisionRecallDisplay.from_estimator(
    classifier, X_test, y_test, name="LinearSVC", plot_chance_level=True
)
_ = display.ax_.set_title("2-class Precision-Recall curve")

# Utilizando el método from_predictions
y_score = classifier.decision_function(X_test)

display = PrecisionRecallDisplay.from_predictions(
    y_test, y_score, name="LinearSVC", plot_chance_level=True
)
_ = display.ax_.set_title("2-class Precision-Recall curve")
```
