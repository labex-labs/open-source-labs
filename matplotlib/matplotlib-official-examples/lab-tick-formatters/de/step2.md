# Einfache Formatierung

In diesem Schritt werden wir zeigen, wie eine einfache Formatierung verwendet wird, indem eine Zeichenfolge oder eine Funktion an `~.Axis.set_major_formatter` oder `~.Axis.set_minor_formatter` übergeben wird. Wir werden zwei Graphen erstellen, einen mit einem Zeichenfolgen-Formatter und einen mit einem Funktions-Formatter.

```python
fig0, axs0 = plt.subplots(2, 1, figsize=(8, 2))
fig0.suptitle('Simple Formatting')

# Eine ``str``, die die Syntax der Formatierungszeichenfolgefunktion verwendet,
# kann direkt als Formatter verwendet werden. Die Variable ``x`` ist der Tick-Wert
# und die Variable ``pos`` ist die Tick-Position. Dies erstellt automatisch einen
# StrMethodFormatter.
setup(axs0[0], title="'{x} km'")
axs0[0].xaxis.set_major_formatter('{x} km')

# Eine Funktion kann ebenfalls direkt als Formatter verwendet werden. Die Funktion
# muss zwei Argumente akzeptieren: ``x`` für den Tick-Wert und ``pos`` für die
# Tick-Position und muss eine ``str`` zurückgeben. Dies erstellt automatisch einen
# FuncFormatter.
setup(axs0[1], title="lambda x, pos: str(x-5)")
axs0[1].xaxis.set_major_formatter(lambda x, pos: str(x-5))

fig0.tight_layout()
```
