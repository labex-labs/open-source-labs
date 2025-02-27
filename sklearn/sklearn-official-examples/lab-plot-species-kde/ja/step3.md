# データを準備する

ここでは、核密度推定のためのデータを準備します。データセットから緯度と経度の情報を抽出し、ラジアンに変換します。

```python
Xtrain = np.vstack([data["train"]["dd lat"], data["train"]["dd long"]]).T
ytrain = np.array(
    [d.decode("ascii").startswith("micro") for d in data["train"]["species"]],
    dtype="int",
)
Xtrain *= np.pi / 180.0  # Convert lat/long to radians
```
