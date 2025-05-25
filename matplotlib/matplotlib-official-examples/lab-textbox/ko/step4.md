# 텍스트 상자 위젯 생성

텍스트 상자 (Textbox) 위젯을 생성하여 그림에 추가합니다. `on_submit` 메서드는 사용자가 텍스트 상자에서 Enter 키를 누르거나 텍스트 상자를 벗어날 때 `submit` 함수를 트리거하는 데 사용됩니다. 또한 텍스트 상자 위젯의 초기 값을 `t ** 2`로 설정합니다.

```python
axbox = fig.add_axes([0.1, 0.05, 0.8, 0.075])
text_box = TextBox(axbox, "Evaluate", textalignment="center")
text_box.on_submit(submit)
text_box.set_val("t ** 2")  # Trigger `submit` with the initial string.
```
