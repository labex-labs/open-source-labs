# 创建数据透视表

创建一个数据透视表，以找出每个监测站中二氧化氮（𝑁𝑂2）和细颗粒物（𝑃𝑀2.5）的平均浓度。

```python
air_quality.pivot_table(
    values="value", index="location", columns="parameter", aggfunc="mean"
)
```
