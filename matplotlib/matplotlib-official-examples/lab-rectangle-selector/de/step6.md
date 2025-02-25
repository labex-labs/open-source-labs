# Erstellen der RectangleSelector- und EllipseSelector-Widgets

Wir werden die RectangleSelector- und EllipseSelector-Widgets erstellen und sie zu den Teilplots hinzufügen.

```python
selectors = []
for ax, selector_class in zip(axs, [RectangleSelector, EllipseSelector]):
    ax.set_title(f"Klicken und ziehen, um ein {selector_class.__name__} zu zeichnen.")
    selectors.append(selector_class(
        ax, select_callback,
        useblit=True,
        button=[1, 3],  # deaktiviere mittlere Taste
        minspanx=5, minspany=5,
        spancoords='pixels',
        interactive=True))
    fig.canvas.mpl_connect('key_press_event', toggle_selector)
axs[0].set_title("Drücken Sie 't', um die Selektoren ein- und auszuschalten.\n"
                 + axs[0].get_title())
```
