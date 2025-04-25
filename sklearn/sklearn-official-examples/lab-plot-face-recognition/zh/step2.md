# 加载并探索数据集

```python
lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)
n_samples, h, w = lfw_people.images.shape
X = lfw_people.data
n_features = X.shape[1]
y = lfw_people.target
target_names = lfw_people.target_names
n_classes = target_names.shape[0]
```

我们使用 scikit-learn 中的`fetch_lfw_people()`函数下载数据集。然后，我们通过获取图像的样本数量、高度和宽度来探索数据集。我们还获取输入数据`X`、目标`y`、目标名称`target_names`和类别数量`n_classes`。
