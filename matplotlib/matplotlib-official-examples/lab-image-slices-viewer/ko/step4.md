# 플롯 생성 및 스크롤 이벤트 연결

Matplotlib 의 `subplots` 함수를 사용하여 플롯을 생성하고 생성된 `IndexTracker` 객체를 전달합니다. 그런 다음 `mpl_connect`를 사용하여 스크롤 이벤트를 figure canvas 에 연결합니다.

```python
fig, ax = plt.subplots()
tracker = IndexTracker(ax, X)

fig.canvas.mpl_connect('scroll_event', tracker.on_scroll)
plt.show()
```
