# Zeichnen der Präzision-Rekall-Kurve

Um die Präzision-Rekall-Kurve zu zeichnen, verwenden wir die PrecisionRecallDisplay-Klasse aus der sklearn.metrics-Bibliothek. Wir können entweder die from_estimator- oder die from_predictions-Methode verwenden, um die Kurve zu berechnen. Die from_estimator-Methode berechnet die Vorhersagen für uns, bevor die Kurve gezeichnet wird, während die from_predictions-Methode erfordert, dass wir die vorhergesagten Scores angeben.

```python
from sklearn.metrics import PrecisionRecallDisplay

# Verwendung der from_estimator-Methode
display = PrecisionRecallDisplay.from_estimator(
    classifier, X_test, y_test, name="LinearSVC", plot_chance_level=True
)
_ = display.ax_.set_title("2-class Precision-Recall curve")

# Verwendung der from_predictions-Methode
y_score = classifier.decision_function(X_test)

display = PrecisionRecallDisplay.from_predictions(
    y_test, y_score, name="LinearSVC", plot_chance_level=True
)
_ = display.ax_.set_title("2-class Precision-Recall curve")
```
