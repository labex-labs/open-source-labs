# 创建宿主轴和寄生轴

我们将使用 `host_subplot()` 和 `twinx()` 函数创建一个宿主轴和两个寄生轴。`host_subplot()` 函数创建一个宿主轴，而 `twinx()` 函数创建与宿主轴共享相同 x 轴的寄生轴。

```python
host = host_subplot(111, axes_class=axisartist.Axes)
plt.subplots_adjust(right=0.75)

par1 = host.twinx()
par2 = host.twinx()
```
