# 加载MRI图像数据

我们将使用`matplotlib`中的`get_sample_data`函数来加载示例MRI图像。该图像为256x256的16位整数格式。

```python
with cbook.get_sample_data('s1045.ima.gz') as dfile:
    im = np.frombuffer(dfile.read(), np.uint16).reshape((256, 256))
```
