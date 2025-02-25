# Fügen einer Farbskala zur Grafik hinzu

Jetzt werden wir einer jeden Teilgrafik eine Farbskala hinzufügen, indem wir die `make_axes_locatable`-Funktion von Matplotlib verwenden. Diese Funktion nimmt eine vorhandene Achse, fügt sie einem neuen `AxesDivider` hinzu und gibt den `AxesDivider` zurück. Die `append_axes`-Methode des `AxesDivider` kann dann verwendet werden, um eine neue Achse auf einer angegebenen Seite ("oben", "rechts", "unten" oder "links") der ursprünglichen Achse zu erstellen.

```python
ax1_divider = make_axes_locatable(ax1)
cax1 = ax1_divider.append_axes("right", size="7%", pad="2%")
cb1 = fig.colorbar(im1, cax=cax1)

ax2_divider = make_axes_locatable(ax2)
cax2 = ax2_divider.append_axes("top", size="7%", pad="2%")
cb2 = fig.colorbar(im2, cax=cax2, orientation="horizontal")
cax2.xaxis.set_ticks_position("top")
```
