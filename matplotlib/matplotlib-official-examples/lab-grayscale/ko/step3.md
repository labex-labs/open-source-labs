# Color Cycle 예제 함수 정의

`color_cycle_example` 함수를 정의합니다. 이 함수는 축 객체를 입력으로 받아 color cycle 의 각 색상에 대한 사인파를 플롯합니다. color cycle 은 rcParams 에 의해 정의됩니다.

```python
def color_cycle_example(ax):
    L = 6
    x = np.linspace(0, L)
    ncolors = len(plt.rcParams['axes.prop_cycle'])
    shift = np.linspace(0, L, ncolors, endpoint=False)
    for s in shift:
        ax.plot(x, np.sin(x + s), 'o-')
```
