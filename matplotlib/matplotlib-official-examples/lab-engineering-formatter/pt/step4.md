# Rotular os Ticks Usando Notação de Engenharia

Agora rotularemos os ticks no eixo x usando notação de engenharia. No primeiro subplot, usaremos as configurações padrão, e no segundo subplot, usaremos as opções `places` e `sep` para especificar o número de dígitos após a vírgula decimal e o separador entre o número e o prefixo/unidade.

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
