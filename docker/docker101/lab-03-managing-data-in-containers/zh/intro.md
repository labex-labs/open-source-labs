# 简介

默认情况下，容器内创建的所有文件都存储在可写的容器层上。这意味着：

- 如果容器不再存在，数据将会丢失。
- 容器的可写层与主机紧密耦合。
- 要管理文件系统，你需要一个使用 Linux 内核提供联合文件系统的存储驱动程序。与直接写入文件系统的「数据卷」相比，这种额外的抽象会降低性能。

Docker 提供了两种将文件存储在主机中的选项：「卷」（volumes）和「绑定挂载」（bind mounts）。如果你在 Linux 上运行 Docker，还可以使用「临时文件系统挂载」（tmpfs mount）；在 Windows 上运行 Docker 时，也可以使用「命名管道」（named pipe）。

![挂载类型](../assets/types-of-mounts.png)

- 「卷」存储在由 Docker 管理的主机文件系统中。
- 「绑定挂载」可以存储在主机系统的任何位置。
- 「临时文件系统挂载」仅存储在主机内存中。

最初，`--mount`标志用于 Docker Swarm 服务，`--volume`标志用于独立容器。从 Docker 17.06 及更高版本开始，你也可以将`--mount`用于独立容器，并且它通常比`--volume`更明确、更详细。

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
这是一个实验（Guided Lab），提供逐步指导来帮助你学习和实践。请仔细按照说明完成每个步骤，获得实际操作经验。根据历史数据，这是一个 <span class="text-green-600 dark:text-green-400">初级</span> 级别的实验，完成率为 <span class="text-green-600 dark:text-green-400">100%</span>。获得了学习者 <span class="text-primary-600 dark:text-primary-400">100%</span> 的好评率。
</div>
