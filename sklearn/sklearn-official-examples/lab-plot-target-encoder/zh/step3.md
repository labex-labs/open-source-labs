# 原生类别特征支持

在本节中，我们构建并评估一个管道，该管道在 `HistGradientBoostingRegressor` 中使用原生类别特征支持，`HistGradientBoostingRegressor` 仅支持多达 255 个唯一类别。我们将类别特征分为低基数特征和高基数特征。高基数特征将进行目标编码，低基数特征将在梯度提升中使用原生类别特征。
