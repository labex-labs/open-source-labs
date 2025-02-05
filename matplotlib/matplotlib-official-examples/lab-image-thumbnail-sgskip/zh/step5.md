# 创建输出目录

在这一步中，你将创建一个名为 `thumbs` 的目录，用于保存缩略图。如果该目录已经存在，则不会再次创建。

```python
outdir = Path("thumbs")
outdir.mkdir(parents=True, exist_ok=True)
```
