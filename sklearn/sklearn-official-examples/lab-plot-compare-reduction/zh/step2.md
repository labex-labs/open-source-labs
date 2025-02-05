# 创建管道并定义参数网格

我们将创建一个管道，该管道先进行降维，然后使用支持向量分类器进行预测。我们将使用无监督的主成分分析（PCA）和非负矩阵分解（NMF）进行降维，并在网格搜索期间进行单变量特征选择。

```python
pipe = Pipeline(
    [
        ("scaling", MinMaxScaler()),
        # 降维阶段由param_grid填充
        ("reduce_dim", "passthrough"),
        ("classify", LinearSVC(dual=False, max_iter=10000)),
    ]
)

N_FEATURES_OPTIONS = [2, 4, 8]
C_OPTIONS = [1, 10, 100, 1000]
param_grid = [
    {
        "reduce_dim": [PCA(iterated_power=7), NMF(max_iter=1_000)],
        "reduce_dim__n_components": N_FEATURES_OPTIONS,
        "classify__C": C_OPTIONS,
    },
    {
        "reduce_dim": [SelectKBest(mutual_info_classif)],
        "reduce_dim__k": N_FEATURES_OPTIONS,
        "classify__C": C_OPTIONS,
    },
]
reducer_labels = ["PCA", "NMF", "KBest(mutual_info_classif)"]
```
