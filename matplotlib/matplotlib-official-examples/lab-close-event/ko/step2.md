# Figure 생성 및 Close 이벤트 연결

이 단계에서는 figure 를 생성하고 close 이벤트를 Step 1 에서 정의한 `on_close` 함수에 연결합니다. 이는 figure 의 canvas 의 `mpl_connect` 메서드를 사용하여 수행됩니다.

```python
fig = plt.figure()
fig.canvas.mpl_connect('close_event', on_close)
```
