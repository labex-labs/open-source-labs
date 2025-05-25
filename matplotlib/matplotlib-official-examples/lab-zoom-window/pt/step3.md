# Conectar o evento à função

Agora, conectamos o evento de pressionar o botão na primeira janela à função on_press que acabamos de definir.

```python
figsrc.canvas.mpl_connect('button_press_event', on_press)
```
