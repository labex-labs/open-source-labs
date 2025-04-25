# K-Means モデルをフィットさせる

画像データの小さなサブサンプルに K-Means モデルをフィットさせ、それを使って画像全体の色インデックスを予測します。

```python
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
from time import time

n_colors = 64

# データの小さなサブサンプルに K-Means モデルをフィットさせる
print("Fitting model on a small sub-sample of the data")
t0 = time()
image_array_sample = shuffle(image_array, random_state=0, n_samples=1000)
kmeans = KMeans(n_clusters=n_colors, n_init="auto", random_state=0).fit(
    image_array_sample
)
print(f"done in {time() - t0:0.3f}s.")

# すべての点に対するラベルを取得する
print("Predicting color indices on the full image (k-means)")
t0 = time()
labels = kmeans.predict(image_array)
print(f"done in {time() - t0:0.3f}s.")
```
