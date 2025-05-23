# 解读结果

我们可以观察到，在集成模型中增加树的数量时，HGBT 和 RF 模型的性能都会提高。然而，分数会达到一个平稳期，此时添加新树只会使拟合和评分变慢。RF 模型更早达到这样的平稳期，并且永远无法达到最大 HGBDT 模型的测试分数。在“测试分数与训练速度的权衡”方面，HGBT 模型始终优于 RF 模型，并且在“测试分数与预测速度”的权衡上，HGBT 模型也更具优势。无论是使用默认超参数还是包括超参数调整成本，HGBT 几乎总是比 RF 提供更有利的速度 - 准确性权衡。
