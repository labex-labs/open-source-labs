# Создание пользовательской функции проверки попадания

В этом шаге мы определим пользовательский подборщик, установив picker равным вызываемой функции. Функция будет определять, попадает ли мышью на художника. Если событие мыши происходит над художником, мы вернем hit=True, а props - это словарь свойств, которые вы хотите добавить к атрибутам `.PickEvent`.

```python
def line_picker(line, mouseevent):
    """
    Найти точки в определенном расстоянии от щелчка мыши в
    координатах данных и прикрепить некоторые дополнительные атрибуты, pickx и picky
    которые являются точками данных, которые были выбраны.
    """
    if mouseevent.xdata is None:
        return False, dict()
    xdata = line.get_xdata()
    ydata = line.get_ydata()
    maxd = 0.05
    d = np.sqrt(
        (xdata - mouseevent.xdata)**2 + (ydata - mouseevent.ydata)**2)

    ind, = np.nonzero(d <= maxd)
    if len(ind):
        pickx = xdata[ind]
        picky = ydata[ind]
        props = dict(ind=ind, pickx=pickx, picky=picky)
        return True, props
    else:
        return False, dict()


def onpick2(event):
    print('onpick2 line:', event.pickx, event.picky)


fig, ax = plt.subplots()
ax.set_title('custom picker for line data')
line, = ax.plot(rand(100), rand(100), 'o', picker=line_picker)
fig.canvas.mpl_connect('pick_event', onpick2)
```
