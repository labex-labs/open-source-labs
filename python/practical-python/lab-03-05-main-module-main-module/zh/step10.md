# 程序退出

程序退出通过异常来处理。

```python
raise SystemExit
raise SystemExit(exitcode)
raise SystemExit('Informative message')
```

另一种方式。

```python
import sys
sys.exit(exitcode)
```

非零的退出代码表示错误。
