# 总结

在本教程中，我们学习了如何使用 `matplotlib.backend_managers.ToolManager` 修改工具栏、创建自定义工具、添加工具以及移除工具。我们创建了一个名为 `ListTools` 的自定义工具，它列出了由 `ToolManager` 控制的所有工具。我们还创建了一个名为 `GroupHideTool` 的自定义工具，它根据工具是启用还是禁用，将绘图上所有具有指定 `gid` 的线条的可见性设置为 `True` 或 `False`。最后，我们将自定义工具添加到 `ToolManager` 中，将 `Show` 工具添加到工具栏中，并从工具栏中移除了“前进”按钮。
