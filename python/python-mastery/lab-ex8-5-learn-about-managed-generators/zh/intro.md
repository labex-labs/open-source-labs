# 简介

在这个实验中，你将了解托管生成器（managed generators），并掌握以非常规方式驱动它们的方法。你还将构建一个简单的任务调度器，并使用生成器创建一个网络服务器。

Python 中的生成器函数需要外部代码来执行。例如，迭代生成器只有在使用 `for` 循环进行迭代时才会运行，而协程则需要调用其 `send()` 方法。在这个实验中，我们将探索在高级应用中驱动生成器的实际示例。本实验期间创建的文件是 `multitask.py` 和 `server.py`。

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
这是一个实验（Guided Lab），提供逐步指导来帮助你学习和实践。请仔细按照说明完成每个步骤，获得实际操作经验。根据历史数据，这是一个 <span class="text-green-600 dark:text-green-400">初级</span> 级别的实验，完成率为 <span class="text-green-600 dark:text-green-400">84%</span>。获得了学习者 <span class="text-primary-600 dark:text-primary-400">80%</span> 的好评率。
</div>
