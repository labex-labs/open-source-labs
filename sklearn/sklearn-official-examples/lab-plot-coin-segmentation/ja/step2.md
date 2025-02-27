# 画像を辺の勾配値付きのグラフに変換する

画像を辺の勾配値付きのグラフに変換します。betaの値が小さいほど、分割は実際の画像から独立します。beta=1の場合、分割はボロノイ分割に近くなります。

```python
# Convert the image into a graph with the value of the gradient on the
# edges.
graph = image.img_to_graph(rescaled_coins)

# Take a decreasing function of the gradient: an exponential
beta = 10
eps = 1e-6
graph.data = np.exp(-beta * graph.data / graph.data.std()) + eps
```
