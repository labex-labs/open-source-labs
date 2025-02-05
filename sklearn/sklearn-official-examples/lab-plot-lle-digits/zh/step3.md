# 比较嵌入技术

我们将使用不同的方法比较不同的嵌入技术。我们将存储投影后的数据以及执行每次投影所需的计算时间。

```python
from sklearn.decomposition import TruncatedSVD
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import RandomTreesEmbedding
from sklearn.manifold import (
    Isomap,
    LocallyLinearEmbedding,
    MDS,
    SpectralEmbedding,
    TSNE,
)
from sklearn.neighbors import NeighborhoodComponentsAnalysis
from sklearn.pipeline import make_pipeline
from sklearn.random_projection import SparseRandomProjection

embeddings = {
    "随机投影嵌入": SparseRandomProjection(
        n_components=2, random_state=42
    ),
    "截断奇异值分解嵌入": TruncatedSVD(n_components=2),
    "线性判别分析嵌入": LinearDiscriminantAnalysis(
        n_components=2
    ),
    "等距映射嵌入": Isomap(n_neighbors=n_neighbors, n_components=2),
    "标准局部线性嵌入": LocallyLinearEmbedding(
        n_neighbors=n_neighbors, n_components=2, method="standard"
    ),
    "修正局部线性嵌入": LocallyLinearEmbedding(
        n_neighbors=n_neighbors, n_components=2, method="modified"
    ),
    "海森局部线性嵌入": LocallyLinearEmbedding(
        n_neighbors=n_neighbors, n_components=2, method="hessian"
    ),
    "局部切空间对准局部线性嵌入": LocallyLinearEmbedding(
        n_neighbors=n_neighbors, n_components=2, method="ltsa"
    ),
    "多维缩放嵌入": MDS(
        n_components=2, n_init=1, max_iter=120, n_jobs=2, normalized_stress="auto"
    ),
    "随机树嵌入": make_pipeline(
        RandomTreesEmbedding(n_estimators=200, max_depth=5, random_state=0),
        TruncatedSVD(n_components=2),
    ),
    "谱嵌入": SpectralEmbedding(
        n_components=2, random_state=0, eigen_solver="arpack"
    ),
    "t-SNE嵌入": TSNE(
        n_components=2,
        n_iter=500,
        n_iter_without_progress=150,
        n_jobs=2,
        random_state=0
    ),
    "邻域成分分析嵌入": NeighborhoodComponentsAnalysis(
        n_components=2, init="pca", random_state=0
    ),
}

projections, timing = {}, {}
for name, transformer in embeddings.items():
    if name.startswith("线性判别分析"):
        data = X.copy()
        data.flat[:: X.shape[1] + 1] += 0.01  # 使X可逆
    else:
        data = X

    print(f"计算 {name}...")
    start_time = time()
    projections[name] = transformer.fit_transform(data, y)
    timing[name] = time() - start_time
```
