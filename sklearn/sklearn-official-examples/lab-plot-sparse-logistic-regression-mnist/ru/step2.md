# Загрузка набора данных MNIST

Мы будем загружать набор данных MNIST с использованием функции `fetch_openml` из scikit-learn. Также мы выберем подмножество данных, установив количество `train_samples` равным 5000.

```python
# Turn down for faster convergence
t0 = time.time()
train_samples = 5000

# Load data from https://www.openml.org/d/554
X, y = fetch_openml(
    "mnist_784", version=1, return_X_y=True, as_frame=False, parser="pandas"
)
```
