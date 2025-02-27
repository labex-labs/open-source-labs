# Parameter definieren

In diesem Schritt definieren wir die Parameter, die zur Darstellung der Entscheidungsflächen auf dem Iris-Datensatz erforderlich sind.

```python
# Parameters
n_classes = 3
n_estimators = 30
cmap = plt.cm.RdYlBu
plot_step = 0.02  # feine Schrittweite für die Konturen der Entscheidungsfläche
plot_step_coarser = 0.5  # Schrittweiten für grobe Klassifizierungsvorhersagen
RANDOM_SEED = 13  # Fixieren des Zufallsziels bei jeder Iteration
```
