# 显示平均每秒帧数

第六步是使用运行动画所花费的总时间来显示平均每秒帧数（FPS）。

```python
print('Average FPS: %f' % (100 / (time.time() - tstart)))
```
