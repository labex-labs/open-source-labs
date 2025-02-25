# Setzen der x-Begrenzungen mit Skalaren oder Maßen

In diesem Schritt werden wir die x-Begrenzungen mit Skalaren oder Maßen festlegen. Wir werden die `set_xlim`-Methode verwenden, um die x-Begrenzungen zu setzen. Wir werden die x-Begrenzungen auf 2 und 6 mit Skalaren in den aktuellen Maßen für das Balkendiagramm in der zweiten Zeile und der ersten Spalte setzen. Wir werden die x-Begrenzungen auf 2 cm und 6 cm mit Maßen für das Balkendiagramm in der zweiten Zeile und der zweiten Spalte setzen.

```python
axs[1, 0].bar(cms, cms, bottom=bottom, width=width, xunits=inch, yunits=cm)
axs[1, 0].set_xlim(2, 6)

axs[1, 1].bar(cms, cms, bottom=bottom, width=width, xunits=inch, yunits=inch)
axs[1, 1].set_xlim(2 * cm, 6 * cm)
```
