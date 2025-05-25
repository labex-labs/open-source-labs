# 사인 곡선 생성

기본 색상 순환 (color cycle) 에서 색상을 사용하여 사인 곡선을 생성합니다.

```python
# 사인 곡선 생성
L = 2*np.pi
x = np.linspace(0, L)
ncolors = len(plt.rcParams['axes.prop_cycle'])
shift = np.linspace(0, L, ncolors, endpoint=False)

for s in shift:
    plt.plot(x, np.sin(x + s), '-')
plt.margins(0)
plt.show()
```
