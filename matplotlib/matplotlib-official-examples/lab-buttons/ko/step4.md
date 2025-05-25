# `Next` 및 `Previous` 버튼 생성

이제 `matplotlib.pyplot`의 `add_axes` 함수를 사용하여 `Next` 및 `Previous` 버튼을 생성하고, 앞서 생성한 콜백 함수들을 `on_clicked`를 사용하여 할당합니다.

```python
axprev = fig.add_axes([0.7, 0.05, 0.1, 0.075])
axnext = fig.add_axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(callback.next)
bprev = Button(axprev, 'Previous')
bprev.on_clicked(callback.prev)
```
