# Einrichten der Label Spreading-Klassifizierer

Wir werden drei Label Spreading-Klassifizierer mit unterschiedlichen Prozentsätzen markierter Daten einrichten: 30%, 50% und 100%. Label Spreading ist ein halbüberwachtes Lernverfahren, das die Labels von markierten auf unmarkierte Datenpunkte basierend auf ihrer Ähnlichkeit weiterverbreitet.

```python
from sklearn.semi_supervised import LabelSpreading

# Einrichten der Label Spreading-Klassifizierer
rng = np.random.RandomState(0)
y_rand = rng.rand(y.shape[0])
y_30 = np.copy(y)
y_30[y_rand < 0.3] = -1  # setze zufällige Stichproben als unmarkiert
y_50 = np.copy(y)
y_50[y_rand < 0.5] = -1
ls30 = (LabelSpreading().fit(X, y_30), y_30, "Label Spreading 30% Daten")
ls50 = (LabelSpreading().fit(X, y_50), y_50, "Label Spreading 50% Daten")
ls100 = (LabelSpreading().fit(X, y), y, "Label Spreading 100% Daten")
```
