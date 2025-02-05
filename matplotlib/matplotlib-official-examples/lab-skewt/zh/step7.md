# 准备数据

我们将为斜 T - 对数 P 图准备数据。我们会使用 StringIO 模块从字符串读取数据，并使用 NumPy 将其加载到数组中。

```python
data_txt = '''
        978.0    345    7.8    0.8
        971.0    404    7.2    0.2
        946.7    610    5.2   -1.8
     ...
    '''
sound_data = StringIO(data_txt)
p, h, T, Td = np.loadtxt(sound_data, unpack=True)
```
