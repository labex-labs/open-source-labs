# 툴바에 버튼 추가

```python
button = Gtk.Button(label='Click me')
button.connect('clicked', lambda button: print('hi mom'))
button.set_tooltip_text('Click me for fun and profit')
toolbar.append(button)
```

레이블 (label) 과 툴팁 (tooltip) 이 있는 버튼을 생성하고, 콘솔에 메시지를 출력하는 함수에 연결합니다. 버튼을 툴바에 추가합니다.
