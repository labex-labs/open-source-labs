# 设置初始参数

我们为模拟设置初始参数，包括时间步长`dt`、步数`num_steps`以及`x`、`y`和`z`的初始值。

```python
dt = 0.01
num_steps = 10000

xyzs = np.empty((num_steps + 1, 3))  # 需要多一个位置来存放初始值
xyzs[0] = (0., 1., 1.05)  # 设置初始值
```
