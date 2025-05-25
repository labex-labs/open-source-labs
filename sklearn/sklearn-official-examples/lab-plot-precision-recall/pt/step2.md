# Plotar a Curva Precisão-Revocação

Para plotar a curva Precisão-Revocação, usaremos a classe `PrecisionRecallDisplay` da biblioteca `sklearn.metrics`. Podemos usar o método `from_estimator` ou `from_predictions` para calcular a curva. O método `from_estimator` calcula as previsões para nós antes de plotar a curva, enquanto o método `from_predictions` requer que forneçamos as pontuações previstas.

```python
from sklearn.metrics import PrecisionRecallDisplay

# Usando o método from_estimator
display = PrecisionRecallDisplay.from_estimator(
    classifier, X_test, y_test, name="LinearSVC", plot_chance_level=True
)
_ = display.ax_.set_title("Curva Precisão-Revocação de 2 classes")

# Usando o método from_predictions
y_score = classifier.decision_function(X_test)

display = PrecisionRecallDisplay.from_predictions(
    y_test, y_score, name="LinearSVC", plot_chance_level=True
)
_ = display.ax_.set_title("Curva Precisão-Revocação de 2 classes")
```
