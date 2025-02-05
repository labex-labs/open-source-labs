# 关于导入的说明

导入方式的变化**不会**改变模块的工作方式。

```python
import math
# 与
import math as m
# 与
from math import cos, sin
...
```

具体来说，`import` 总是会执行**整个**文件，并且模块仍然是隔离的环境。

`import module as` 语句只是在本地更改名称。`from math import cos, sin` 语句在幕后仍然会加载整个 `math` 模块。它只是在完成后将 `cos` 和 `sin` 名称从模块复制到本地空间。
