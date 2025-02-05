# 设置启动选项

你可以在 Python/IPython 环境中创建一个启动脚本，用于导入 pandas 并设置选项，这能让使用 pandas 更加高效。

```python
# 这是一个启动脚本的示例
# 将此脚本放在 IPython 配置文件的启动目录下的一个.py 文件中
import pandas as pd

pd.set_option("display.max_rows", 999)
pd.set_option("display.precision", 5)
```
