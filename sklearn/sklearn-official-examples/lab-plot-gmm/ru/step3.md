# Реализуем модель смеси Гауссовых распределений

В этом шаге мы реализуем модель смеси Гауссовых распределений с использованием класса `GaussianMixture` из scikit-learn. Мы подберем параметры модели для нашего набора данных и предскажем метки кластеров для каждой точки данных. Наконец, мы построим результаты.

```python
# Create a GMM object with 5 components
gmm = mixture.GaussianMixture(n_components=5, covariance_type="full")

# Fit the GMM to the data
gmm.fit(X)

# Predict the cluster labels
Y_ = gmm.predict(X)

# Plot the results
color_iter = ["navy", "c", "cornflowerblue", "gold", "darkorange"]

for i, color in enumerate(color_iter):
    plt.scatter(
        X[Y_ == i, 0], X[Y_ == i, 1], 0.8, color=color, label="Cluster {}".format(i)
    )

plt.legend(loc="best")
plt.title("Gaussian Mixture Model")
plt.show()
```
