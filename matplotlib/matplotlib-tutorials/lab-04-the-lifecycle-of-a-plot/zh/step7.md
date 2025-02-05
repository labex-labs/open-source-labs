# 保存绘图

最后，我们可以将绘图保存到磁盘。请按以下步骤操作：

1. 使用 `print(fig.canvas.get_supported_filetypes())` 打印支持的文件格式。

```python
print(fig.canvas.get_supported_filetypes())
```

2. 使用 `fig.savefig(file_path, transparent=False, dpi=80, bbox_inches="tight")` 将图形保存为图像文件。取消注释此行以保存图形。

```python
fig.savefig('sales.png', transparent=False, dpi=80, bbox_inches="tight")
```

你可以使用左侧边栏中的文件资源管理器打开保存的图像文件。
