# 设置写入器

我们需要设置用于将帧写入文件的写入器。我们设置每秒帧数（fps）并添加诸如标题、作者和注释等元数据。

```python
metadata = dict(title='Movie Test', artist='Matplotlib',
                comment='Movie support!')
writer = FFMpegWriter(fps=15, metadata=metadata)
```
