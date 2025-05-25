# 콜백 함수 정의

체크 버튼에 대한 콜백 함수를 정의해야 합니다. 이 함수는 체크 버튼을 클릭할 때마다 호출됩니다. 이 함수를 사용하여 플롯에서 해당 선의 가시성을 토글합니다.

```python
def callback(label):
    ln = lines_by_label[label]
    ln.set_visible(not ln.get_visible())
    ln.figure.canvas.draw_idle()

check.on_clicked(callback)
```
