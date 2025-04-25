# 学习图像字典

我们使用 MiniBatchKMeans 来学习图像字典。我们将聚类数设置为 81，设置随机状态，并启用详细模式。然后，我们创建一个缓冲区来存储图像块，并遍历数据集中的每一张图像。我们从每张图像中提取 50 个图像块并重塑数据。然后，我们将数据追加到缓冲区并增加索引。如果索引是 10 的倍数，我们将连接缓冲区并对数据运行 partial_fit。如果索引是 100 的倍数，我们将打印一条消息，指示到目前为止已经拟合的图像块数量。

```python
import time
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.feature_extraction.image import extract_patches_2d

print("Learning the dictionary... ")
rng = np.random.RandomState(0)
kmeans = MiniBatchKMeans(n_clusters=81, random_state=rng, verbose=True, n_init=3)
patch_size = (20, 20)

buffer = []
t0 = time.time()

# The online learning part: cycle over the whole dataset 6 times
index = 0
for _ in range(6):
    for img in faces.images:
        data = extract_patches_2d(img, patch_size, max_patches=50, random_state=rng)
        data = np.reshape(data, (len(data), -1))
        buffer.append(data)
        index += 1
        if index % 10 == 0:
            data = np.concatenate(buffer, axis=0)
            data -= np.mean(data, axis=0)
            data /= np.std(data, axis=0)
            kmeans.partial_fit(data)
            buffer = []
        if index % 100 == 0:
            print("Partial fit of %4i out of %i" % (index, 6 * len(faces.images)))

dt = time.time() - t0
print("done in %.2fs." % dt)
```
