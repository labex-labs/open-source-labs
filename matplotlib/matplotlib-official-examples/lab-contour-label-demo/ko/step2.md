# 사용자 정의 레벨 포맷터로 등고선 레이블 만들기

이제 사용자 정의 레벨 포맷터로 등고선 레이블을 만들 것입니다. 이를 통해 레이블을 특정 방식으로 서식 지정할 수 있습니다. 이 경우, 후행 0 을 제거하고 백분율 기호를 추가합니다.

```python
def fmt(x):
    s = f"{x:.1f}"
    if s.endswith("0"):
        s = f"{x:.0f}"
    return rf"{s} \%" if plt.rcParams["text.usetex"] else f"{s} %"

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, CS.levels, inline=True, fmt=fmt, fontsize=10)
```
