# Daten generieren

Zunächst müssen wir einige Beispiel-Daten generieren, die wir verwenden können, um unsere Modelle anzupassen. Wir werden numpy verwenden, um 100 Stichproben zu generieren, jede mit 30 Merkmalen und 40 Aufgaben. Wir werden auch 5 relevante Merkmale zufällig auswählen und für sie Koeffizienten mit Sinuswellen mit zufälliger Frequenz und Phase erstellen. Schließlich werden wir einigen zufälligen Rauschen zu den Daten hinzufügen.

```python
import numpy as np

rng = np.random.RandomState(42)

# Generieren Sie einige 2D-Koeffizienten mit Sinuswellen mit zufälliger Frequenz und Phase
n_samples, n_features, n_tasks = 100, 30, 40
n_relevant_features = 5
coef = np.zeros((n_tasks, n_features))
times = np.linspace(0, 2 * np.pi, n_tasks)
for k in range(n_relevant_features):
    coef[:, k] = np.sin((1.0 + rng.randn(1)) * times + 3 * rng.randn(1))

X = rng.randn(n_samples, n_features)
Y = np.dot(X, coef.T) + rng.randn(n_samples, n_tasks)
```
