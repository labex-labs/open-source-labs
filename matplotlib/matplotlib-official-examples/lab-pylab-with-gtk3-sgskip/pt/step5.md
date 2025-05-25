# Adicionar Rótulo ao VBox

Adicionaremos um rótulo ao vbox para exibir as coordenadas x,y do mouse quando ele for arrastado sobre os eixos. Primeiro, criamos um rótulo com algum texto e o adicionamos ao vbox.

```python
label = Gtk.Label()
label.set_markup('Drag mouse over axes for position')
label.show()
vbox.pack_start(label, False, False, 0)
```
