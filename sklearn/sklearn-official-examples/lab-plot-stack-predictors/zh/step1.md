# 下载数据集

我们将使用艾姆斯房屋数据集（Ames Housing dataset），该数据集最初由迪恩·德·科克（Dean De Cock）汇编，在被用于 Kaggle 挑战（Kaggle challenge）后变得更广为人知。它是爱荷华州艾姆斯市的 1460 套住宅的集合，每套住宅由 80 个特征描述。我们将用它来预测房屋的最终对数价格。在这个例子中，我们将只使用通过梯度提升回归器（GradientBoostingRegressor()）选择的 20 个最相关的特征，并限制条目数量。
