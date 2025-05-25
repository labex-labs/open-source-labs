# 레이블이 있는 간단한 등고선 플롯 생성

이제 데이터를 갖추었으므로 기본 색상을 사용하여 레이블이 있는 간단한 등고선 플롯을 만들 수 있습니다.

```python
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Simplest default with labels')
```
