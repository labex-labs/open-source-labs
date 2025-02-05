# 动态导入

现在你准备好攻克最后一关了。完全删除以下导入语句：

```python
# formatter.py
...

from.formats.text import TextTableFormatter     # DELETE
from.formats.csv import CSVTableFormatter       # DELETE
from.formats.html import HTMLTableFormatter     # DELETE
...
```

再次运行你的 `stock.py` 代码 —— 它应该会因错误而失败。它对文本格式化器一无所知。通过在 `create_formatter()` 中添加以下一小段代码来修复它：

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    if name not in TableFormatter._formats:
        __import__(f'{__package__}.formats.{name}')
  ...
```

如果对名称一无所知，这段代码会尝试动态导入格式化器模块。仅导入操作（如果成功）就会将类注册到 `_formats` 字典中，然后一切就都能正常工作了。神奇吧！

尝试运行 `stock.py` 代码，并确保之后它能正常运行。
