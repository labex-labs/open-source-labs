# 툴바 (Toolbar) 에 버튼 추가

Gtk 모듈을 사용하여 툴바 (toolbar) 에 버튼을 추가합니다. 먼저, 레이블 (label) 이 있는 버튼을 생성하고, 클릭 시 메시지를 출력하는 함수에 연결합니다. 그런 다음, toolitem 을 생성하고, 툴팁 텍스트를 설정하고, 버튼을 추가하고, 툴바에 삽입합니다.

```python
button = Gtk.Button(label='Click me')
button.show()
button.connect('clicked', lambda button: print('hi mom'))

toolitem = Gtk.ToolItem()
toolitem.show()
toolitem.set_tooltip_text('Click me for fun and profit')
toolitem.add(button)

pos = 8  # where to insert this in the toolbar
toolbar.insert(toolitem, pos)
```
