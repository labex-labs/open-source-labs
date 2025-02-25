# Crear el widget de Cuadro de Texto

Creamos el widget de Cuadro de Texto y lo agregamos a la figura. El método `on_submit` se utiliza para desencadenar la función `submit` cuando el usuario presiona la tecla Enter en el cuadro de texto o sale del cuadro de texto. También establecemos el valor inicial del widget de Cuadro de Texto en `t ** 2`.

```python
axbox = fig.add_axes([0.1, 0.05, 0.8, 0.075])
text_box = TextBox(axbox, "Evaluate", textalignment="center")
text_box.on_submit(submit)
text_box.set_val("t ** 2")  # Trigger `submit` with the initial string.
```
