# 2D 히스토그램 그리기

2D 히스토그램을 그리려면 히스토그램의 각 축에 해당하는 동일한 길이의 두 개의 벡터만 있으면 됩니다.

```python
fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(dist1, dist2)

plt.show()
```
