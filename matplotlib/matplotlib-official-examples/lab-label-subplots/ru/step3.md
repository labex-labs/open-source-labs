# Метка внутри осей

Самый простой способ подписать подграфики - это поместить метку внутри осей. Мы можем это сделать, используя метод `ax.text`. Мы пройдем по каждому подграфику и добавим метку внутри осей с использованием `ax.transAxes`.

```python
for label, ax in axs.items():
    # label physical distance in and down:
    trans = mtransforms.ScaledTranslation(10/72, -5/72, fig.dpi_scale_trans)
    ax.text(0.0, 1.0, label, transform=ax.transAxes + trans,
            fontsize='medium', verticalalignment='top', fontfamily='serif',
            bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
```
