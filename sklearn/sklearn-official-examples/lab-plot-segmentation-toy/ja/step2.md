# 画像をグラフに変換する

画像をグラフに変換するために、`sklearn.feature_extraction.image` の `img_to_graph` を使います。辺の勾配の値も計算されます。

```python
from sklearn.feature_extraction import image

graph = image.img_to_graph(img, mask=mask)
```
