# 散布図を作成する

ロンドンとパリで測定された NO2 の値を視覚的に比較するには、散布図を作成できます。

```python
# Creating a scatter plot
air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
plt.show()
```
