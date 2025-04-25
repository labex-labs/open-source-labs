# 回帰モデルをフィットさせる

次に、5 つの近傍点と一様重みと距離重みの両方を使って、回帰モデルをサンプルデータにフィットさせます。各重みの種類に対して for ループを使って反復処理を行い、データポイントの散布図と、フィットさせたモデルの`predict`メソッドを使った予測値の線グラフを作成します。

```python
n_neighbors = 5

for i, weights in enumerate(["uniform", "distance"]):
    knn = neighbors.KNeighborsRegressor(n_neighbors, weights=weights)
    y_ = knn.fit(X, y).predict(T)

    plt.subplot(2, 1, i + 1)
    plt.scatter(X, y, color="darkorange", label="data")
    plt.plot(T, y_, color="navy", label="prediction")
    plt.axis("tight")
    plt.legend()
    plt.title("KNeighborsRegressor (k = %i, weights = '%s')" % (n_neighbors, weights))

plt.tight_layout()
plt.show()
```
