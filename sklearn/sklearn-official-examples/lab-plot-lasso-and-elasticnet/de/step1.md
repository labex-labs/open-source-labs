# Synthetischen Datensatz generieren

Zunächst generieren wir einen Datensatz, bei dem die Anzahl der Stichproben kleiner ist als die Gesamtzahl der Merkmale. Dies führt zu einem unbestimmten System, d.h., die Lösung ist nicht eindeutig, und wir können eine gewöhnliche kleinste Quadrate-Methode nicht alleine anwenden. Regularisierung führt einen Strafbegriff in die Zielfunktion ein, was das Optimierungsproblem modifiziert und helfen kann, die unbestimmte Natur des Systems zu mildern. Wir werden ein Ziel `y` generieren, das eine lineare Kombination mit abwechselnden Vorzeichen von sinusförmigen Signalen ist. Nur die 10 niedrigsten von den 100 Frequenzen in `X` werden verwendet, um `y` zu generieren, während die restlichen Merkmale nicht informativ sind. Dies führt zu einem hochdimensionalen dünn besetzten Merkmalsraum, in dem ein gewisser Grad an L1-Strafe erforderlich ist.

```python
import numpy as np

rng = np.random.RandomState(0)
n_samples, n_features, n_informative = 50, 100, 10
time_step = np.linspace(-2, 2, n_samples)
freqs = 2 * np.pi * np.sort(rng.rand(n_features)) / 0.01
X = np.zeros((n_samples, n_features))

for i in range(n_features):
    X[:, i] = np.sin(freqs[i] * time_step)

idx = np.arange(n_features)
true_coef = (-1) ** idx * np.exp(-idx / 10)
true_coef[n_informative:] = 0  # sparsify coef
y = np.dot(X, true_coef)

# introduce random phase using numpy.random.random_sample
# add some gaussian noise using numpy.random.normal
for i in range(n_features):
    X[:, i] = np.sin(freqs[i] * time_step + 2 * (rng.random_sample() - 0.5))
    X[:, i] += 0.2 * rng.normal(0, 1, n_samples)

y += 0.2 * rng.normal(0, 1, n_samples)

# split the data into train and test sets using train_test_split from sklearn
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, shuffle=False)
```
