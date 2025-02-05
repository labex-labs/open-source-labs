# 创建一个计算距离的函数

我们需要创建一个函数，用于计算点与线段之间的距离。该函数稍后将用于确定是否应向多边形添加新顶点。

```python
def dist_point_to_segment(p, s0, s1):
    """
    获取点 *p* 到线段 (*s0*, *s1*) 的距离，其中
    *p*, *s0*, *s1* 是 ``[x, y]`` 数组。
    """
    s01 = s1 - s0
    s0p = p - s0
    if (s01 == 0).all():
        return np.hypot(*s0p)
    # 投影到线段上，不超过线段端点。
    p1 = s0 + np.clip((s0p @ s01) / (s01 @ s01), 0, 1) * s01
    return np.hypot(*(p - p1))
```
