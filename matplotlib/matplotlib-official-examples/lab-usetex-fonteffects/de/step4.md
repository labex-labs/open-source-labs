# Erstellen des Diagramms

In diesem Schritt werden wir das Diagramm erstellen. Wir werden die `fig.text()`-Methode verwenden, um Text zum Diagramm hinzuzufügen. Wir werden über eine Liste von Schriften und entsprechendem Text iterieren, wobei die `zip()`-Funktion verwendet wird, um sie zuzuordnen. Wir werden den `usetex`-Parameter auf `True` setzen, um den usetex-Modus zu aktivieren.

```python
fig = plt.figure()
for y, font, text in zip(
    range(5),
    ['ptmr8r', 'ptmri8r', 'ptmro8r', 'ptmr8rn', 'ptmrr8re'],
    [f'Nimbus Roman No9 L {x}'
     for x in ['', 'Italics (real italics for comparison)',
               '(slanted)', '(condensed)', '(extended)']],
):
    fig.text(.1, 1 - (y + 1) / 6, setfont(font) + text, usetex=True)

fig.suptitle('Usetex font effects')
plt.show()
```
