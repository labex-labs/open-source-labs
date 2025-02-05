# 验证目录

在这一步中，你将检查指定的目录是否存在。如果目录不存在，你将退出程序并打印一条错误消息。

```python
if not args.imagedir.is_dir():
    sys.exit(f"Could not find input directory {args.imagedir}")
```
