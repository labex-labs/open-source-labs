# 简介

随机梯度下降（Stochastic Gradient Descent，SGD）是机器学习中一种常用的优化算法。它是梯度下降算法的一种变体，在每次迭代时使用随机选择的训练数据子集。这使得它在计算上效率很高，适合处理大型数据集。在本实验中，我们将逐步介绍如何使用 scikit-learn 在 Python 中实现 SGD。

## 虚拟机使用提示

虚拟机启动完成后，点击左上角切换到**笔记本**标签页，以访问 Jupyter Notebook 进行练习。

有时，你可能需要等待几秒钟让 Jupyter Notebook 完成加载。由于 Jupyter Notebook 的限制，操作验证无法自动化。

如果你在学习过程中遇到问题，随时向 Labby 提问。课程结束后提供反馈，我们会及时为你解决问题。

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
这是一个实验（Guided Lab），提供逐步指导来帮助你学习和实践。请仔细按照说明完成每个步骤，获得实际操作经验。根据历史数据，这是一个 <span class="text-green-600 dark:text-green-400">初级</span> 级别的实验，完成率为 <span class="text-green-600 dark:text-green-400">82%</span>。获得了学习者 <span class="text-primary-600 dark:text-primary-400">100%</span> 的好评率。
</div>
