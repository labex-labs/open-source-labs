# 解析参数

在这一步中，你将解析传递给程序的参数。你需要创建一个 `ArgumentParser` 对象，并添加一个名为 `imagedir` 的参数。此参数指定包含图像的目录的路径。你可以使用 `type` 参数来指定参数的数据类型。在这种情况下，参数应为 `Path` 类型。

```python
parser = ArgumentParser(description="Build thumbnails of all images in a directory.")
parser.add_argument("imagedir", type=Path)
args = parser.parse_args()
```
