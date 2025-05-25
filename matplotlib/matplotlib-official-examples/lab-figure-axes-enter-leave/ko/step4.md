# 이벤트 핸들러를 Figure Canvas 에 연결

이제 `mpl_connect` 메서드를 사용하여 이벤트 핸들러를 figure canvas 에 연결합니다. 이렇게 하면 마우스가 figure 또는 axes 에 들어가거나 나갈 때 이벤트 핸들러가 트리거됩니다.

```python
fig.canvas.mpl_connect('figure_enter_event', on_enter_figure)
fig.canvas.mpl_connect('figure_leave_event', on_leave_figure)
fig.canvas.mpl_connect('axes_enter_event', on_enter_axes)
fig.canvas.mpl_connect('axes_leave_event', on_leave_axes)
```
