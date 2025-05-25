# draw 이벤트 (event) 를 콜백 함수에 연결

`draw_event`를 `on_draw` 함수에 연결해야 합니다.

```python
fig.canvas.mpl_connect('draw_event', on_draw)
```
