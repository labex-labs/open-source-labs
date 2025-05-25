# 레이블 추가

이 단계에서는 데이터를 플롯 (plot) 하기 위해 행을 더블 클릭하라는 메시지를 사용자에게 표시하는 레이블을 윈도우에 추가합니다.

```python
vbox = Gtk.VBox(homogeneous=False, spacing=8)
self.add(vbox)
label = Gtk.Label(label='Double click a row to plot the data')
vbox.pack_start(label, False, False, 0)
```
