# 启用写时复制

首先，让我们在pandas中启用CoW。这可以通过使用pandas中的`copy_on_write`配置选项来完成。以下是两种可以全局启用CoW的方法。

```python
# 导入pandas和numpy库
import pandas as pd

# 使用set_option启用CoW
pd.set_option("mode.copy_on_write", True)

# 或者直接赋值
pd.options.mode.copy_on_write = True
```
