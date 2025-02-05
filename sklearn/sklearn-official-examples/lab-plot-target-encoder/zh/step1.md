# 从 OpenML 加载数据

首先，我们使用 scikit-learn.datasets 模块中的 `fetch_openml` 函数加载葡萄酒评论数据集。我们将仅使用数据中的一部分数值和类别特征。我们将在数据中使用以下数值和类别特征子集：`numerical_features = ["price"]` 和 `categorical_features = ["country", "province", "region_1", "region_2", "variety", "winery"]`。
