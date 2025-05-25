# `ToolManager`에 의해 제어되는 모든 도구 나열

첫 번째 단계는 `ToolManager`에 의해 제어되는 모든 도구를 나열하는 것입니다. 이는 `ListTools`라는 사용자 정의 도구를 생성하여 수행할 수 있습니다. `ListTools` 클래스는 `ToolBase`를 상속합니다. `ListTools`의 `trigger()` 메서드는 사용 가능한 모든 도구의 이름, 설명 및 키맵을 출력합니다.

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
