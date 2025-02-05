# 总结

在本实验中，我们使用了 Scikit-Learn 的 `VotingClassifier` 基于两个特征来预测鸢尾花的类别。我们训练了三个分类器：`DecisionTreeClassifier`、`KNeighborsClassifier` 和 `SVC`。然后，我们使用 `VotingClassifier` 来组合它们的预测结果并绘制了决策边界。我们发现 `VotingClassifier` 的决策边界与 `SVC` 的决策边界相似，但在某些区域的复杂度较低。
