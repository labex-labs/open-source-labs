# 축 (spines) 끝에 화살표 그리기

축의 방향을 나타내기 위해 축 (spines) 의 끝에 화살표를 그릴 수 있습니다.

```python
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
```
