# Erstellen des Textfeld-Widgets

Wir erstellen das Textfeld-Widget und fügen es zur Figur hinzu. Die `on_submit`-Methode wird verwendet, um die `submit`-Funktion auszulösen, wenn der Benutzer in das Textfeld die Eingabetaste drückt oder das Textfeld verlässt. Wir setzen auch den Anfangswert des Textfeld-Widgets auf `t ** 2`.

```python
axbox = fig.add_axes([0.1, 0.05, 0.8, 0.075])
text_box = TextBox(axbox, "Evaluate", textalignment="center")
text_box.on_submit(submit)
text_box.set_val("t ** 2")  # Trigger `submit` with the initial string.
```
