# `__main__` 检查

作为主脚本运行的模块通常采用以下约定：

```python
# prog.py
...
if __name__ == '__main__':
    # 作为主程序运行时……
    语句
  ...
```

`if` 语句内包含的语句将成为主程序。
