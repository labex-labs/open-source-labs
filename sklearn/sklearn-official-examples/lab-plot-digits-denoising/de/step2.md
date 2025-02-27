# Erstelle Trainings- und Testsets

Wir teilen den Datensatz in einen Trainingssatz mit 1000 Proben und einen Testsatz mit 100 Proben auf. Wir fügen Gaussian-Rauschen (Gauß'sches Rauschen) zum Testsatz hinzu und erstellen zwei Kopien der ursprünglichen Daten; eine mit Rauschen und eine ohne Rauschen.

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, random_state=0, train_size=1_000, test_size=100
)

rng = np.random.RandomState(0)
noise = rng.normal(scale=0.25, size=X_test.shape)
X_test_noisy = X_test + noise

noise = rng.normal(scale=0.25, size=X_train.shape)
X_train_noisy = X_train + noise
```
