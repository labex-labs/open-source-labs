# Synthetisches Dataset generieren

Wir generieren ein synthetisches Dataset, in dem `X` und `y` linear verknüpft sind. Zehn der Features von `X` werden verwendet, um `y` zu generieren. Die anderen Features sind bei der Vorhersage von `y` nicht nützlich. Darüber hinaus generieren wir ein Dataset, bei dem `n_samples == n_features`. Ein solcher Einstellung ist für ein OLS-Modell herausfordernd und kann möglicherweise zu beliebig großen Gewichten führen. Ein Vorwissen über die Gewichte und eine Strafe mildern das Problem. Schließlich wird gaussian Rauschen hinzugefügt.

```python
from sklearn.datasets import make_regression

X, y, true_weights = make_regression(
    n_samples=100,
    n_features=100,
    n_informative=10,
    noise=8,
    coef=True,
    random_state=42,
)
```
