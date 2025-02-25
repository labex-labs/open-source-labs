# Definiere die Histogrammfunktion

Wir werden eine Funktion definieren, um ein Histogramm als gestuftes Patch zu zeichnen. Die Funktion nimmt die folgenden Parameter:

- `ax`: Die Achsen, auf denen geplottet werden soll
- `edges`: Ein Array der Länge n+1, das die linken Kanten jedes Bins und die rechte Kante des letzten Bins angibt
- `values`: Ein Array der Länge n mit den Häufigkeiten oder Werten der Bins
- `bottoms`: Ein Float oder Array, optional, ein Array der Länge n mit der unteren Grenze der Balken. Wenn None, wird Null verwendet.
- `orientation`: Ein String, optional, die Ausrichtung des Histogramms. 'v' (Standard) hat die Balken in die positive y-Richtung zunehmend.

```python
def filled_hist(ax, edges, values, bottoms=None, orientation='v', **kwargs):
    """
    Zeichnet ein Histogramm als gestuftes Patch.

    Parameter
    ----------
    ax : Achsen
        Die Achsen, auf denen geplottet werden soll

    Kanten : Array
        Ein Array der Länge n+1, das die linken Kanten jedes Bins und die
        rechte Kante des letzten Bins angibt.

    Werte : Array
        Ein Array der Länge n mit den Häufigkeiten oder Werten der Bins

    Unterkanten : float oder Array, optional
        Ein Array der Länge n mit der unteren Grenze der Balken. Wenn None, wird Null verwendet.

    Orientierung : {'v', 'h'}
        Ausrichtung des Histogramms. 'v' (Standard) hat
        die Balken in die positive y-Richtung zunehmend.

    **kwargs
        Zusätzliche Schlüsselwortargumente werden an `.fill_between` weitergeleitet.

    Rückgabe
    -------
    ret : PolyCollection
        Künstler, der zur Achse hinzugefügt wird
    """
    if orientation not in 'hv':
        raise ValueError(f"Orientierung muss in {{'h', 'v'}} sein, nicht {orientation}")

    kwargs.setdefault('step', 'post')
    kwargs.setdefault('alpha', 0.7)
    Kanten = np.asarray(Kanten)
    Werte = np.asarray(Werte)
    if len(Kanten) - 1!= len(Werte):
        raise ValueError(f'Muss eine Bin-Kante mehr als Wert angeben, nicht: {len(Kanten)=} {len(Werte)=}')

    if Unterkanten ist None:
        Unterkanten = 0
    Unterkanten = np.broadcast_to(Unterkanten, Werte.shape)

    Werte = np.append(Werte, Werte[-1])
    Unterkanten = np.append(Unterkanten, Unterkanten[-1])
    if Orientierung == 'h':
        return ax.fill_betweenx(Kanten, Werte, Unterkanten, **kwargs)
    elif Orientierung == 'v':
        return ax.fill_between(Kanten, Werte, Unterkanten, **kwargs)
    else:
        raise AssertionError("Du solltest nie hier sein")
```
