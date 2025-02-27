# Tracer la frontière de décision discrète

Nous utiliserons la classe `DecisionBoundaryDisplay` pour visualiser une frontière de décision discrète. La couleur d'arrière-plan représente si un échantillon dans cette zone donnée est prédit comme étant une anomalie ou non. Le nuage de points affiche les vraies étiquettes.

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
disp.ax_.set_title("Frontière de décision binaire \nde l'IsolationForest")
plt.axis("square")
plt.legend(handles=handles, labels=["anomalies", "données normales"], title="classe réelle")
plt.show()
```
