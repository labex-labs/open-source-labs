# Criar o Widget Textbox

Criamos o widget Textbox e o adicionamos à figura. O método `on_submit` é usado para acionar a função `submit` quando o usuário pressiona Enter no textbox ou sai do textbox. Também definimos o valor inicial do widget Textbox para `t ** 2`.

```python
axbox = fig.add_axes([0.1, 0.05, 0.8, 0.075])
text_box = TextBox(axbox, "Evaluate", textalignment="center")
text_box.on_submit(submit)
text_box.set_val("t ** 2")  # Trigger `submit` with the initial string.
```
