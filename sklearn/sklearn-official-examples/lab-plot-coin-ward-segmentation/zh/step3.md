# 计算聚类

定义好数据和连通性矩阵后，我们现在可以进行层次聚类了。我们将使用 scikit-learn 的 `AgglomerativeClustering` 类来执行聚类。我们将把聚类数量设置为 27，这是图像中硬币的数量。我们将使用 “ward” 链接方法，该方法会最小化正在合并的聚类之间距离的方差。我们还将传入在第二步中创建的连通性矩阵。

```python
from sklearn.cluster import AgglomerativeClustering
import time as time

print("Compute structured hierarchical clustering...")
st = time.time()
n_clusters = 27  # number of regions
ward = AgglomerativeClustering(
    n_clusters=n_clusters, linkage="ward", connectivity=connectivity
)
ward.fit(X)
label = np.reshape(ward.labels_, rescaled_coins.shape)
print(f"Elapsed time: {time.time() - st:.3f}s")
print(f"Number of pixels: {label.size}")
print(f"Number of clusters: {np.unique(label).size}")
```
