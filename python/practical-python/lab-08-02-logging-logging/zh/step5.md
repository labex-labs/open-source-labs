# 日志记录配置

日志记录行为是单独配置的。

```python
# main.py

...

if __name__ == '__main__':
    import logging
    logging.basicConfig(
        filename  = 'app.log',      # 日志输出文件
        level     = logging.INFO,   # 输出级别
    )
```

通常，这是在程序启动时进行的一次性配置。该配置与进行日志记录调用的代码是分开的。
