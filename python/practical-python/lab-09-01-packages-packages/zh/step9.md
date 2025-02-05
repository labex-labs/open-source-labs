# 脚本的另一种解决方案

如前所述，现在你需要使用 `-m package.module` 来运行包内的脚本。

```bash
$ python3 -m porty.pcost portfolio.csv
```

还有另一种选择：编写一个新的顶级脚本。

```python
#!/usr/bin/env python3
# pcost.py
import porty.pcost
import sys
porty.pcost.main(sys.argv)
```

此脚本位于包**外部**。例如，查看目录结构：

    pcost.py       # 顶级脚本
    porty/         # 包目录
        __init__.py
        pcost.py
      ...
