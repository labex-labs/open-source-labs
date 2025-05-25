# 산점도 생성

무작위로 생성된 데이터를 사용하여 산점도를 생성합니다.

```python
np.random.seed(19680801)
data = np.random.rand(100, 2)

subplot_kw = dict(xlim=(0, 1), ylim=(0, 1), autoscale_on=False)
fig, ax = plt.subplots(subplot_kw=subplot_kw)
pts = ax.scatter(data[:, 0], data[:, 1], s=80)
selector = SelectFromCollection(ax, pts)
```
