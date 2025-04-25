# Textbox ウィジェットを作成する

Textbox ウィジェットを作成し、グラフに追加します。`on_submit`メソッドは、ユーザーがテキストボックスで Enter キーを押すか、テキストボックスを離れたときに`submit`関数をトリガーします。また、TextBox ウィジェットの初期値を`t ** 2`に設定します。

```python
axbox = fig.add_axes([0.1, 0.05, 0.8, 0.075])
text_box = TextBox(axbox, "Evaluate", textalignment="center")
text_box.on_submit(submit)
text_box.set_val("t ** 2")  # Trigger `submit` with the initial string.
```
