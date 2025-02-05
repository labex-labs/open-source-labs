# 列出由 `ToolManager` 控制的所有工具

第一步是列出由 `ToolManager` 控制的所有工具。这可以通过创建一个名为 `ListTools` 的自定义工具来实现。`ListTools` 类继承自 `ToolBase`。`ListTools` 的 `trigger()` 方法会打印所有可用工具的名称、描述和快捷键映射。

```python
class ListTools(ToolBase):
    """列出由 `ToolManager` 控制的所有工具。"""
    default_keymap = 'm'  # 键盘快捷键
    description = '列出工具'

    def trigger(self, *args, **kwargs):
        print('_' * 80)
        fmt_tool = "{:12} {:45} {}".format
        print(fmt_tool('名称 (id)', '工具描述', '快捷键映射'))
        print('-' * 80)
        tools = self.toolmanager.tools
        for name in sorted(tools):
            if not tools[name].description:
                continue
            keys = ', '.join(sorted(self.toolmanager.get_tool_keymap(name)))
            print(fmt_tool(name, tools[name].description, keys))
        print('_' * 80)
        fmt_active_toggle = "{!s:12} {!s:45}".format
        print("活动切换工具")
        print(fmt_active_toggle("组", "活动状态"))
        print('-' * 80)
        for group, active in self.toolmanager.active_toggle.items():
            print(fmt_active_toggle(group, active))
```
