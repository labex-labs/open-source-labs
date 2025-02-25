# Créer le tracé

Dans cette étape, nous allons créer le tracé. Nous utiliserons la méthode `fig.text()` pour ajouter du texte au tracé. Nous allons itérer sur une liste de polices et de texte correspondant, en utilisant la fonction `zip()` pour les associer. Nous allons définir le paramètre `usetex` sur `True` pour activer le mode usetex.

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
