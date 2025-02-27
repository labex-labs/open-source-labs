# Tracer la courbe Précision-Rappel

Pour tracer la courbe Précision-Rappel, nous utiliserons la classe PrecisionRecallDisplay du module sklearn.metrics. Nous pouvons utiliser soit la méthode from_estimator soit la méthode from_predictions pour calculer la courbe. La méthode from_estimator calcule les prédictions pour nous avant de tracer la courbe, tandis que la méthode from_predictions nous demande de fournir les scores prédits.

```python
from sklearn.metrics import PrecisionRecallDisplay

# Utilisation de la méthode from_estimator
display = PrecisionRecallDisplay.from_estimator(
    classifier, X_test, y_test, name="LinearSVC", plot_chance_level=True
)
_ = display.ax_.set_title("Courbe Précision-Rappel à 2 classes")

# Utilisation de la méthode from_predictions
y_score = classifier.decision_function(X_test)

display = PrecisionRecallDisplay.from_predictions(
    y_test, y_score, name="LinearSVC", plot_chance_level=True
)
_ = display.ax_.set_title("Courbe Précision-Rappel à 2 classes")
```
