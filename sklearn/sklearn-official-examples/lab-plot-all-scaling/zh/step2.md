# 选择特征并定义特征映射

接下来，我们从数据集中选择两个特征，以便于可视化，并定义特征名称的映射，以实现更好的可视化效果。

```python
# 选择两个特征
features = ["MedInc", "AveOccup"]
features_idx = [feature_names.index(feature) for feature in features]
X = X_full[:, features_idx]

# 定义特征映射
feature_mapping = {
    "MedInc": "街区中位数收入",
    "AveOccup": "房屋平均入住率",
}
```
