# Python Matplotlib Tool Manager Tutorial

## Introduction

This tutorial will show you how to modify the Toolbar, create tools, add tools, and remove tools using `matplotlib.backend_managers.ToolManager`.

## Steps

### Step 1: List all the tools controlled by the `ToolManager`

The first step is to list all the tools controlled by the `ToolManager`. This can be achieved by creating a custom tool named `ListTools`. The `ListTools` class inherits from `ToolBase`. The `trigger()` method of `ListTools` prints the name, description and keymap of all the available tools.

```python
class ListTools(ToolBase):
    """List all the tools controlled by the `ToolManager`."""
    default_keymap = 'm'  # keyboard shortcut
    description = 'List Tools'

    def trigger(self, *args, **kwargs):
        print('_' * 80)
        fmt_tool = "{:12} {:45} {}".format
        print(fmt_tool('Name (id)', 'Tool description', 'Keymap'))
        print('-' * 80)
        tools = self.toolmanager.tools
        for name in sorted(tools):
            if not tools[name].description:
                continue
            keys = ', '.join(sorted(self.toolmanager.get_tool_keymap(name)))
            print(fmt_tool(name, tools[name].description, keys))
        print('_' * 80)
        fmt_active_toggle = "{!s:12} {!s:45}".format
        print("Active Toggle tools")
        print(fmt_active_toggle("Group", "Active"))
        print('-' * 80)
        for group, active in self.toolmanager.active_toggle.items():
            print(fmt_active_toggle(group, active))
```

### Step 2: Show lines with a given gid

The second step is to create a custom tool named `GroupHideTool`. The `GroupHideTool` class inherits from `ToolToggleBase`. The `set_lines_visibility()` method of `GroupHideTool` sets the visibility of all the lines on the plot which have the specified `gid` to either True or False, depending on whether the tool is enabled or disabled.

```python
class GroupHideTool(ToolToggleBase):
    """Show lines with a given gid."""
    default_keymap = 'S'
    description = 'Show by gid'
    default_toggled = True

    def __init__(self, *args, gid, **kwargs):
        self.gid = gid
        super().__init__(*args, **kwargs)

    def enable(self, *args):
        self.set_lines_visibility(True)

    def disable(self, *args):
        self.set_lines_visibility(False)

    def set_lines_visibility(self, state):
        for ax in self.figure.get_axes():
            for line in ax.get_lines():
                if line.get_gid() == self.gid:
                    line.set_visible(state)
        self.figure.canvas.draw()
```

### Step 3: Add custom tools

The third step is to add the custom tools that we created in steps 1 and 2. This can be achieved by calling the `add_tool()` method of the `ToolManager`. We add the `ListTools` and `GroupHideTool` tools to the `ToolManager`. We also add the `Show` tool to the `Toolbar`, which was created using the `add_tool()` method of `Toolbar`.

```python
fig.canvas.manager.toolmanager.add_tool('List', ListTools)
fig.canvas.manager.toolmanager.add_tool('Show', GroupHideTool, gid='mygroup')
fig.canvas.manager.toolbar.add_tool('Show', 'navigation', 1)
```

### Step 4: Remove tools

The fourth step is to remove the `forward` button from the `Toolbar`. We can achieve this by calling the `remove_tool()` method of the `ToolManager`.

```python
fig.canvas.manager.toolmanager.remove_tool('forward')
```

## Summary

In this tutorial, we learned how to modify the Toolbar, create custom tools, add tools, and remove tools using `matplotlib.backend_managers.ToolManager`. We created a custom tool named `ListTools`, which lists all the tools controlled by the `ToolManager`. We also created a custom tool named `GroupHideTool`, which sets the visibility of all the lines on the plot which have the specified `gid` to either True or False, depending on whether the tool is enabled or disabled. Finally, we added the custom tools to the `ToolManager`, added the `Show` tool to the `Toolbar`, and removed the `forward` button from the `Toolbar`.
