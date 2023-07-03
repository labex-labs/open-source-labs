# Summary

In this tutorial, we learned how to modify the Toolbar, create custom tools, add tools, and remove tools using `matplotlib.backend_managers.ToolManager`. We created a custom tool named `ListTools`, which lists all the tools controlled by the `ToolManager`. We also created a custom tool named `GroupHideTool`, which sets the visibility of all the lines on the plot which have the specified `gid` to either True or False, depending on whether the tool is enabled or disabled. Finally, we added the custom tools to the `ToolManager`, added the `Show` tool to the `Toolbar`, and removed the `forward` button from the `Toolbar`.