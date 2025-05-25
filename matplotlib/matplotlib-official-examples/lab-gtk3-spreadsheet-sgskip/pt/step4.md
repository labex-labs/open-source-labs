# Adicionar um Rótulo (Label)

Nesta etapa, adicionaremos um rótulo (label) à janela que solicitará ao usuário que clique duas vezes em uma linha para plotar os dados.

```python
vbox = Gtk.VBox(homogeneous=False, spacing=8)
self.add(vbox)
label = Gtk.Label(label='Double click a row to plot the data')
vbox.pack_start(label, False, False, 0)
```
