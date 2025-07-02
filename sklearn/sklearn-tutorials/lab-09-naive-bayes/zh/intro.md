# 简介

在本实验中，我们将通过一个示例来学习如何在 Python 中使用 scikit-learn 库中的朴素贝叶斯分类器。朴素贝叶斯分类器是一组常用于分类任务的监督学习算法。这些分类器基于应用贝叶斯定理，并假设在给定类别变量值的情况下，每对特征之间具有条件独立性。

在本示例中，我们将使用 scikit-learn 中的高斯朴素贝叶斯分类器对鸢尾花数据集进行分类，这是一个在机器学习中很受欢迎的数据集。目标是根据鸢尾花的花瓣和萼片尺寸预测其品种。

## 虚拟机使用提示

虚拟机启动完成后，点击左上角切换到“笔记本”标签页，以访问 Jupyter Notebook 进行练习。

有时，你可能需要等待几秒钟让 Jupyter Notebook 完成加载。由于 Jupyter Notebook 的限制，操作验证无法自动化。

如果你在学习过程中遇到问题，随时向 Labby 提问。课程结束后提供反馈，我们会及时为你解决问题。

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
这是一个实验（Guided Lab），提供逐步指导来帮助你学习和实践。请仔细按照说明完成每个步骤，获得实际操作经验。根据历史数据，这是一个 <span class="text-green-600 dark:text-green-400">初级</span> 级别的实验，完成率为 <span class="text-green-600 dark:text-green-400">91%</span>。获得了学习者 <span class="text-primary-600 dark:text-primary-400">100%</span> 的好评率。
</div>
