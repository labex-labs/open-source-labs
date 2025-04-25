# 特徴量の選択と特徴量マッピングの定義

次に、データセットから 2 つの特徴量を選択して可視化を容易にし、より良い可視化のために特徴量名のマッピングを定義します。

```python
# Select two features
features = ["MedInc", "AveOccup"]
features_idx = [feature_names.index(feature) for feature in features]
X = X_full[:, features_idx]

# Define feature mapping
feature_mapping = {
    "MedInc": "Median income in block",
    "AveOccup": "Average house occupancy",
}
```
