# 이벤트 핸들러 연결

이벤트 핸들러를 figure canvas 에 연결합니다.

```python
browser = PointBrowser()

fig.canvas.mpl_connect('pick_event', browser.on_pick)
fig.canvas.mpl_connect('key_press_event', browser.on_press)
```
