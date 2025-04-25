# ガウス混合モデルの実装

このステップでは、scikit - learn の`GaussianMixture`クラスを使ってガウス混合モデルを実装します。このモデルをデータセットに適合させ、各データポイントのクラスタラベルを予測します。最後に、結果をプロットします。

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
