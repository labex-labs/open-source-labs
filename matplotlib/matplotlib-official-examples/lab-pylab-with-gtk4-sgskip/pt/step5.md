# Adicionar um rótulo ao canvas

```python
label = Gtk.Label()
label.set_markup('Drag mouse over axes for position')
vbox.insert_child_after(label, fig.canvas)
```

Criamos um rótulo e definimos seu texto. Adicionamos o rótulo à caixa vertical (vbox) após o canvas da figura.
