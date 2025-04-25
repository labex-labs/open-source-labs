# 密度推定のプロット

次に、ガウス混合の密度推定をプロットします。データセットの範囲にわたって点のメッシュグリッドを作成し、各点に対して GMM によって予測される負の対数尤度を計算します。その後、予測されたスコアを等高線プロットとして表示し、学習データを散布図で表示します。

```python
# モデルによって予測されたスコアを等高線プロットとして表示する
x = np.linspace(-20.0, 30.0)
y = np.linspace(-20.0, 40.0)
X, Y = np.meshgrid(x, y)
XX = np.array([X.ravel(), Y.ravel()]).T
Z = -clf.score_samples(XX)
Z = Z.reshape(X.shape)

CS = plt.contour(
    X, Y, Z, norm=LogNorm(vmin=1.0, vmax=1000.0), levels=np.logspace(0, 3, 10)
)
CB = plt.colorbar(CS, shrink=0.8, extend="both")
plt.scatter(X_train[:, 0], X_train[:, 1], 0.8)

plt.title("Density Estimation with Gaussian Mixture Models")
plt.axis("tight")
plt.show()
```
