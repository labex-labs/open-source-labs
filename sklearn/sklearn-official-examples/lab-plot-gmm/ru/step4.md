# Реализуем Байесовскую модель смеси Гауссовых распределений

В этом шаге мы реализуем Байесовскую модель смеси Гауссовых распределений с использованием класса `BayesianGaussianMixture` из scikit-learn. Эта модель имеет априорный процесс Дирихле, который автоматически настраивает количество кластеров в зависимости от данных. Мы подберем параметры модели для нашего набора данных и предскажем метки кластеров для каждой точки данных. Наконец, мы построим результаты.

```python
# Create a Bayesian GMM object with 5 components
dpgmm = mixture.BayesianGaussianMixture(n_components=5, covariance_type="full")

# Fit the Bayesian GMM to the data
dpgmm.fit(X)

# Predict the cluster labels
Y_ = dpgmm.predict(X)

# Plot the results
color_iter = ["navy", "c", "cornflowerblue", "gold", "darkorange"]

for i, color in enumerate(color_iter):
    plt.scatter(
        X[Y_ == i, 0], X[Y_ == i, 1], 0.8, color=color, label="Cluster {}".format(i)
    )

plt.legend(loc="best")
plt.title("Bayesian Gaussian Mixture Model with a Dirichlet process prior")
plt.show()
```
