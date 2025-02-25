# Connecter les gestionnaires d'événements à la toile de la figure

Nous allons maintenant connecter les gestionnaires d'événements à la toile de la figure en utilisant la méthode `mpl_connect`. Cela permettra aux gestionnaires d'événements d'être déclenchés lorsque la souris entre ou sort de la figure ou des axes.

```python
fig.canvas.mpl_connect('figure_enter_event', on_enter_figure)
fig.canvas.mpl_connect('figure_leave_event', on_leave_figure)
fig.canvas.mpl_connect('axes_enter_event', on_enter_axes)
fig.canvas.mpl_connect('axes_leave_event', on_leave_axes)
```
