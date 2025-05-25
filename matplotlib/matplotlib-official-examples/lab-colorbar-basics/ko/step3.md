# 양수 데이터 플롯 및 컬러바 생성

양수 데이터의 플롯을 생성하고, `colorbar` 함수를 사용하여 플롯에 컬러바를 추가합니다.

```python
# plot just the positive data and save the
# color "mappable" object returned by ax1.imshow
pos = plt.imshow(Zpos, cmap='Blues', interpolation='none')

# add the colorbar using the figure's method,
# telling which mappable we're talking about and
# which axes object it should be near
plt.colorbar(pos)
```
