# 简介

本实验探讨均匀分布的随机标签对某些聚类评估指标行为的影响。聚类算法从根本上来说是无监督学习方法，而评估指标则利用“有监督”的真实信息来量化所得聚类的质量。然而，未经调整的聚类评估指标可能会产生误导，因为对于细粒度标签（可能完全是随机的），它们会输出较大的值。因此，只有经过调整的指标才能安全地用作共识指标，以评估聚类算法在数据集的各种重叠子样本上对于给定 k 值的平均稳定性。

## 虚拟机使用提示

虚拟机启动完成后，点击左上角切换到“笔记本”标签页，以访问 Jupyter Notebook 进行练习。

有时，你可能需要等待几秒钟让 Jupyter Notebook 完成加载。由于 Jupyter Notebook 的限制，操作验证无法自动化。

如果你在学习过程中遇到问题，随时向 Labby 提问。课程结束后提供反馈，我们会及时为你解决问题。

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
这是一个实验（Guided Lab），提供逐步指导来帮助你学习和实践。请仔细按照说明完成每个步骤，获得实际操作经验。根据历史数据，这是一个 <span class="text-red-600 dark:text-red-400">高级</span> 级别的实验，完成率为 <span class="text-red-600 dark:text-red-400">31%</span>。获得了学习者 <span class="text-primary-600 dark:text-primary-400">100%</span> 的好评率。
</div>
