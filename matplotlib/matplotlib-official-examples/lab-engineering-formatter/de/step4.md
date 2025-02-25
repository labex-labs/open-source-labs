# Skalenmarkierungen mit Engineering-Notation bezeichnen

Wir werden nun die Skalenmarkierungen auf der x-Achse mit der Engineering-Notation bezeichnen. Im ersten Teilplot werden wir die Standardeinstellungen verwenden, und im zweiten Teilplot werden wir die Optionen `places` und `sep` verwenden, um die Anzahl der Nachkommastellen und den Separator zwischen der Zahl und dem Präfix/Einheit anzugeben.

```python
# Demo of the default settings, with a user-defined unit label.
ax0.set_title('Full unit ticklabels, w/ default precision & space separator')
formatter0 = EngFormatter(unit='Hz')
ax0.xaxis.set_major_formatter(formatter0)
ax0.plot(xs, ys)
ax0.set_xlabel('Frequency')

# Demo of the options `places` (number of digit after decimal point) and
# `sep` (separator between the number and the prefix/unit).
ax1.set_title('SI-prefix only ticklabels, 1-digit precision & '
              'thin space separator')
formatter1 = EngFormatter(places=1, sep="\N{THIN SPACE}")  # U+2009
ax1.xaxis.set_major_formatter(formatter1)
ax1.plot(xs, ys)
ax1.set_xlabel('Frequency [Hz]')
```
