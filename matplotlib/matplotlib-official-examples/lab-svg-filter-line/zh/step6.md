# 定义滤镜

我们使用带有 `stdDeviation` 属性的 `<defs>` 和 `<filter>` 标签来定义高斯模糊滤镜。

```python
filter_def = """
  <defs xmlns='http://www.w3.org/2000/svg'
        xmlns:xlink='http://www.w3.org/1999/xlink'>
    <filter id='dropshadow' height='1.2' width='1.2'>
      <feGaussianBlur result='blur' stdDeviation='3'/>
    </filter>
  </defs>
"""
```
