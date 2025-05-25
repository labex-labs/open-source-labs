# 플롯 생성

다음으로, Matplotlib 의 `subplots()` 함수를 사용하여 플롯을 생성하고 시간에 따른 Google 주식의 조정 종가를 플롯합니다.

```python
fig, ax = plt.subplots()
ax.plot(r.date, r.adj_close)
```
