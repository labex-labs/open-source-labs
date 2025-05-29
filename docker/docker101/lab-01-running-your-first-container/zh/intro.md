# 简介

在本实验中，你将运行你的第一个 Docker 容器。

容器只是一个隔离运行的进程（或一组进程）。隔离是通过 Linux 命名空间、控制组（cgroups）、seccomp 和 SELinux 实现的。请注意，Linux 命名空间和控制组是内置于 Linux 内核中的！除了 Linux 内核本身，容器并没有什么特别之处。

使容器变得有用的是围绕它的工具。对于这些实验，我们将使用 Docker，它是一个被广泛采用的用于使用容器构建应用程序的工具。Docker 为开发者和运维人员提供了一个友好的界面，以便在任何具有 Docker 引擎的环境中构建、交付和运行容器。由于 Docker 客户端需要一个 Docker 引擎，另一种选择是使用 [Podman](https://podman.io/)，它是一个无守护进程的容器引擎，用于开发、管理和运行 [OCI](https://opencontainers.org/) 容器，并且能够以 root 身份或无 root 模式运行容器。出于这些原因，我们推荐使用 Podman，但由于 Docker 的广泛应用，本实验仍使用 Docker。

在本实验的第一部分，我们将运行我们的第一个容器，并学习如何检查它。我们将能够见证从 Linux 内核获得的命名空间隔离。

在运行第一个容器之后，我们将深入探讨容器的其他用途。你可以在 Docker 商店上找到许多这样的示例，并且我们将在同一主机上运行几种不同类型的容器。这将使我们看到隔离的好处——我们可以在同一主机上运行多个容器而不会产生冲突。

在本实验中，我们将使用一些 Docker 命令。有关可用命令的完整文档，请查看 [官方文档](https://docs.docker.com/)。

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
这是一个实验（Guided Lab），提供逐步指导来帮助你学习和实践。请仔细按照说明完成每个步骤，获得实际操作经验。根据历史数据，这是一个 <span class="text-green-600 dark:text-green-400">初级</span> 级别的实验，完成率为 <span class="text-green-600 dark:text-green-400">89.29%</span>。获得了学习者 <span class="text-primary-600 dark:text-primary-400">92.31%</span> 的好评率。
</div>
