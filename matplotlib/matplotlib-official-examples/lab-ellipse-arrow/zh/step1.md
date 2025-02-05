# 导入Matplotlib并创建图形和坐标轴

首先，你需要导入Matplotlib并创建一个图形和坐标轴。图形和坐标轴是你绘图的容器。

```python
import matplotlib.pyplot as plt

# 创建一个图形和坐标轴
fig, ax = plt.subplots(subplot_kw={"aspect": "equal"})
```
