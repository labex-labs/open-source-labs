# 应用程序结构

代码组织和文件结构是应用程序可维护性的关键。

对于Python来说，没有“一刀切”的方法。然而，一种适用于许多问题的结构大致如下。

```code
porty-app/
  README.txt
  script.py         # 脚本
  porty/
    # 库代码
    __init__.py
    pcost.py
    report.py
    fileparse.py
```

顶级目录 `porty-app` 是其他所有内容的容器 —— 文档、顶级脚本、示例等等。

同样，顶级脚本（如果有的话）需要存在于代码包之外，即上一级目录。

```python
#!/usr/bin/env python3
# porty-app/script.py
import sys
import porty

porty.report.main(sys.argv)
```

此时，你有一个包含几个程序的目录：

    pcost.py          # 计算投资组合成本
    report.py         # 生成报告
    ticker.py         # 生成实时股票报价

还有各种具有其他功能的支持模块：

    stock.py          # 股票类
    portfolio.py      # 投资组合类
    fileparse.py      # CSV解析
    tableformat.py    # 格式化表格
    follow.py         # 跟踪日志文件
    typedproperty.py  # 带类型的类属性

在本练习中，我们将清理代码并将其放入一个通用包中。
