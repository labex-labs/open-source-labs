# 데이터 포인트 마스킹 및 산점도 생성

원점으로부터의 거리를 기준으로 데이터 포인트를 마스킹합니다. `r0`보다 작은 거리를 가진 데이터 포인트는 `area1`에서 마스킹되고, `r0`보다 크거나 같은 거리를 가진 데이터 포인트는 `area2`에서 마스킹됩니다. 그런 다음, `area1`과 `area2`에 대해 각각 `marker='^'` 및 `marker='o'`를 사용하여 마스킹된 데이터 포인트의 산점도를 생성합니다.

```python
r = np.sqrt(x ** 2 + y ** 2)
area1 = np.ma.masked_where(r < r0, area)
area2 = np.ma.masked_where(r >= r0, area)
plt.scatter(x, y, s=area1, marker='^', c=c)
plt.scatter(x, y, s=area2, marker='o', c=c)
```
