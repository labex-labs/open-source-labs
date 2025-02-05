# 生成缩略图

在这一步中，你将为指定目录中的所有图像生成缩略图。你将使用一个 `for` 循环来遍历指定目录中所有具有 `.png` 扩展名的图像。对于每一张图像，你将生成一个缩略图并将其保存在 `thumbs` 目录中。

```python
for path in args.imagedir.glob("*.png"):
    outpath = outdir / path.name
    fig = image.thumbnail(path, outpath, scale=0.15)
    print(f"saved thumbnail of {path} to {outpath}")
```
