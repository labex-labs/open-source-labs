# 启用写时复制

首先，让我们在 pandas 中启用 CoW。这可以通过使用 pandas 中的`copy_on_write`配置选项来完成。以下是两种可以全局启用 CoW 的方法。

```python
# 导入 pandas 和 numpy 库
import pandas as pd

# 使用 set_option 启用 CoW
pd.set_option("mode.copy_on_write", True)

# 或者直接赋值
pd.options.mode.copy_on_write = True
```
