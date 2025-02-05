# 拟合K均值模型

我们将在图像数据的一个小子样本上拟合K均值模型，并使用它来预测整个图像的颜色索引。

```python
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
from time import time

n_colors = 64

# 在数据的一个小子样本上拟合K均值模型
print("在数据的一个小子样本上拟合模型")
t0 = time()
image_array_sample = shuffle(image_array, random_state=0, n_samples=1000)
kmeans = KMeans(n_clusters=n_colors, n_init="auto", random_state=0).fit(
    image_array_sample
)
print(f"完成于 {time() - t0:0.3f} 秒。")

# 获取所有点的标签
print("预测整个图像的颜色索引 (k均值)")
t0 = time()
labels = kmeans.predict(image_array)
print(f"完成于 {time() - t0:0.3f} 秒。")
```
