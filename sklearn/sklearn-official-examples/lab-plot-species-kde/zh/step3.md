# 准备数据

现在我们将为核密度估计准备数据。我们将从数据集中提取纬度和经度信息，并将它们转换为弧度。

```python
Xtrain = np.vstack([data["train"]["dd lat"], data["train"]["dd long"]]).T
ytrain = np.array(
    [d.decode("ascii").startswith("micro") for d in data["train"]["species"]],
    dtype="int",
)
Xtrain *= np.pi / 180.0  # Convert lat/long to radians
```
