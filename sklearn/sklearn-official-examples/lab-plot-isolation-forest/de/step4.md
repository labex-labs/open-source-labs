# Zeichne die diskrete Entscheidungsgrenze

Wir werden die Klasse `DecisionBoundaryDisplay` verwenden, um eine diskrete Entscheidungsgrenze zu visualisieren. Die Hintergrundfarbe gibt an, ob eine Probe in einem bestimmten Bereich als Ausreißer vorhergesagt wird oder nicht. Der Streudiagramm zeigt die wahren Labels an.

```python
import matplotlib.pyplot as plt
from sklearn.inspection import DecisionBoundaryDisplay

disp = DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    response_method="predict",
    alpha=0.5,
)
disp.ax_.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor="k")
disp.ax_.set_title("Binäre Entscheidungsgrenze \nvon IsolationForest")
plt.axis("square")
plt.legend(handles=handles, labels=["Ausreißer", "Innerpunkte"], title="wahre Klasse")
plt.show()
```
