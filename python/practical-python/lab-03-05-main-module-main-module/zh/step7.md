# 命令行参数

命令行是一个文本字符串列表。

```bash
$ python3 report.py portfolio.csv prices.csv
```

这个文本字符串列表可以在 `sys.argv` 中找到。

```python
# 在上一个bash命令中
sys.argv # ['report.py', 'portfolio.csv', 'prices.csv']
```

以下是处理参数的一个简单示例：

```python
import sys

if len(sys.argv)!= 3:
    raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile')
portfile = sys.argv[1]
pricefile = sys.argv[2]
...
```
