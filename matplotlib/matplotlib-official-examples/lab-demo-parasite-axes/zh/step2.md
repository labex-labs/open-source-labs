# 创建一个图形并添加宿主轴

我们使用`plt.figure()`方法创建一个图形，并使用`fig.add_axes()`方法添加一个宿主轴。宿主轴与寄生轴共享x轴刻度。

```python
fig = plt.figure()
host = fig.add_axes([0.15, 0.1, 0.65, 0.8], axes_class=HostAxes)
```
