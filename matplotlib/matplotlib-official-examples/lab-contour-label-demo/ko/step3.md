# 딕셔너리를 사용하여 임의의 문자열로 등고선 레이블 지정

또한 딕셔너리를 사용하여 임의의 문자열로 등고선에 레이블을 지정할 수 있습니다. 이를 통해 사용자 정의 레이블로 등고선에 레이블을 지정할 수 있습니다. 이 예제에서는 문자열 목록을 사용하여 등고선에 레이블을 지정합니다.

```python
fig1, ax1 = plt.subplots()
CS1 = ax1.contour(X, Y, Z)

fmt = {}
strs = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']
for l, s in zip(CS1.levels, strs):
    fmt[l] = s

ax1.clabel(CS1, CS1.levels[::2], inline=True, fmt=fmt, fontsize=10)
```
