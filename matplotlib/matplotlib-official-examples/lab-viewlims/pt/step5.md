# Adicionar funcionalidade de zoom

Adicionaremos a funcionalidade de zoom conectando os eventos xlim_changed e ylim_changed aos objetos UpdatingRect e MandelbrotDisplay.

```python
ax2.callbacks.connect('xlim_changed', rect)
ax2.callbacks.connect('ylim_changed', rect)

ax2.callbacks.connect('xlim_changed', md.ax_update)
ax2.callbacks.connect('ylim_changed', md.ax_update)
ax2.set_title("Zoom aqui")
```
