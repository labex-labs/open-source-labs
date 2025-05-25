# 캔버스에 레이블 추가

```python
label = Gtk.Label()
label.set_markup('Drag mouse over axes for position')
vbox.insert_child_after(label, fig.canvas)
```

레이블을 생성하고 텍스트를 설정합니다. figure canvas 다음에 vbox 에 레이블을 추가합니다.
