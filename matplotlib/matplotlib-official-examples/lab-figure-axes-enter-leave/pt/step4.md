# Conectando os Manipuladores de Eventos ao Canvas da Figura

Agora conectaremos os manipuladores de eventos ao canvas da figura usando o método `mpl_connect`. Isso permitirá que os manipuladores de eventos sejam acionados quando o mouse entrar ou sair da figura ou dos eixos.

```python
fig.canvas.mpl_connect('figure_enter_event', on_enter_figure)
fig.canvas.mpl_connect('figure_leave_event', on_leave_figure)
fig.canvas.mpl_connect('axes_enter_event', on_enter_axes)
fig.canvas.mpl_connect('axes_leave_event', on_leave_axes)
```
