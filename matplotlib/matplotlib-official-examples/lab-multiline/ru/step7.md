# Добавление многострочного текста на второй подграфик

На втором подграфике мы добавим многострочный текст с использованием функции `text`. Мы можем указать позицию, размер, вертикальное и горизонтальное выравнивание и рамку вокруг текста.

```python
ax1.text(0.29, 0.4, "Mat\nTTp\n123", size=18,
         va="baseline", ha="right", multialignment="left",
         bbox=dict(fc="none"))

ax1.text(0.34, 0.4, "Mag\nTTT\n123", size=18,
         va="baseline", ha="left", multialignment="left",
         bbox=dict(fc="none"))

ax1.text(0.95, 0.4, "Mag\nTTT$^{A^A}$\n123", size=18,
         va="baseline", ha="right", multialignment="left",
         bbox=dict(fc="none"))
```
