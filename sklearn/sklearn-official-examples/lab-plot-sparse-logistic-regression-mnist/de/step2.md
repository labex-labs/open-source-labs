# MNIST-Datensatz laden

Wir werden den MNIST-Datensatz mit der Funktion `fetch_openml` aus scikit-learn laden. Wir werden auch einen Teilsatz der Daten auswählen, indem wir die Anzahl der `train_samples` auf 5000 setzen.

```python
# Turn down for faster convergence
t0 = time.time()
train_samples = 5000

# Load data from https://www.openml.org/d/554
X, y = fetch_openml(
    "mnist_784", version=1, return_X_y=True, as_frame=False, parser="pandas"
)
```
