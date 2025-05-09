# 简介

在 Go 语言中，关闭一个通道可用于向通道的接收者传达完成信息。本挑战将演示如何使用通道将 `main()` 协程中待完成的工作传达给工作协程，以及当工作协程没有更多任务时如何关闭通道。

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
这是一个挑战（Challenge），与实验（Lab）不同，你需要独立完成挑战任务，而不是按照实验的步骤学习。挑战通常有一点难度。如果你觉得困难，可以与 Labby 讨论或查看解决方案。
</div>
