# 创建散点图

为了直观地比较在伦敦和巴黎测量的二氧化氮（NO2）值，我们可以创建一个散点图。

```python
# 创建散点图
air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
plt.show()
```
