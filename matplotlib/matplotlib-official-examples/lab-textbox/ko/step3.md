# Submit 함수 정의

사용자가 텍스트 입력을 제출할 때 호출될 `submit` 함수를 정의합니다. 이 함수는 사용자의 입력을 기반으로 플롯된 함수를 업데이트합니다.

```python
def submit(expression):
    """
    Update the plotted function to the new math *expression*.

    *expression* is a string using "t" as its independent variable, e.g.
    "t ** 3".
    """
    ydata = eval(expression, {'np': np}, {'t': t})
    l.set_ydata(ydata)
    ax.relim()
    ax.autoscale_view()
    plt.draw()
```
