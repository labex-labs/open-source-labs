# ベイズ型ガウス混合モデルの実装

このステップでは、scikit - learnの`BayesianGaussianMixture`クラスを使ってベイズ型ガウス混合モデルを実装します。このモデルは、ディリクレ過程事前分布を持ち、データに基づいて自動的にクラスタ数を適応させます。このモデルをデータセットに適合させ、各データポイントのクラスタラベルを予測します。最後に、結果をプロットします。

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
