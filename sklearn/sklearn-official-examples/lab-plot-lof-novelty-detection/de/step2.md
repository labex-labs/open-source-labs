# Daten generieren

Wir werden mit numpy einige Daten für das Training, das Testing und die Ausreißer generieren. Wir werden 100 normale Trainingsbeobachtungen, 20 normale Testbeobachtungen und 20 abnormale neue Beobachtungen generieren.

```python
np.random.seed(42)

xx, yy = np.meshgrid(np.linspace(-5, 5, 500), np.linspace(-5, 5, 500))
X = 0.3 * np.random.randn(100, 2)
X_train = np.r_[X + 2, X - 2]
X = 0.3 * np.random.randn(20, 2)
X_test = np.r_[X + 2, X - 2]
X_outliers = np.random.uniform(low=-4, high=4, size=(20, 2))
```