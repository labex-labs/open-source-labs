# 创建寄生轴

我们使用`host.get_aux_axes()`方法创建两个寄生轴。我们将`viewlim_mode=None`设置为确保寄生轴与宿主轴共享相同的 x 轴刻度。我们还设置`sharex=host`以确保共享 x 轴刻度。

```python
par1 = host.get_aux_axes(viewlim_mode=None, sharex=host)
par2 = host.get_aux_axes(viewlim_mode=None, sharex=host)
```
