# VBox 에 레이블 (Label) 추가

축 위로 마우스를 드래그할 때 마우스의 x, y 좌표를 표시하기 위해 vbox 에 레이블 (label) 을 추가합니다. 먼저, 텍스트가 있는 레이블을 생성하고 vbox 에 추가합니다.

```python
label = Gtk.Label()
label.set_markup('Drag mouse over axes for position')
label.show()
vbox.pack_start(label, False, False, 0)
```
