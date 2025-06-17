# 简介

在本实验中，我们将基于实验 1 的知识展开，在实验 1 中我们使用 Docker 命令来运行容器。我们将从一个 Dockerfile 创建一个自定义的 Docker 镜像。一旦我们构建了镜像，我们会将其推送到一个中央注册表，在那里它可以被拉取以部署到其他环境中。此外，我们将简要描述镜像层，以及 Docker 如何结合“写时复制”和联合文件系统来高效地存储镜像和运行容器。

在本实验中，我们将使用一些 Docker 命令。有关可用命令的完整文档，请查看[官方文档](https://docs.docker.com/)。

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
这是一个实验（Guided Lab），提供逐步指导来帮助你学习和实践。请仔细按照说明完成每个步骤，获得实际操作经验。根据历史数据，这是一个 <span class="text-green-600 dark:text-green-400">初级</span> 级别的实验，完成率为 <span class="text-green-600 dark:text-green-400">82%</span>。获得了学习者 <span class="text-primary-600 dark:text-primary-400">100%</span> 的好评率。
</div>
