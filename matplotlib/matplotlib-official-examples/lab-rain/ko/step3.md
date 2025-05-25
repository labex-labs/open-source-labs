# 산점도 구성

이제 애니메이션 동안 빗방울이 발달함에 따라 업데이트될 산점도 (scatter plot) 를 구성합니다.

```python
scat = ax.scatter(rain_drops['position'][:, 0], rain_drops['position'][:, 1],
                  s=rain_drops['size'], lw=0.5, edgecolors=rain_drops['color'],
                  facecolors='none')
```
