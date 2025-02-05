# Create the Plot

In this step, we will create the plot. We will use the `fig.text()` method to add text to the plot. We will iterate over a list of fonts and corresponding text, using the `zip()` function to match them up. We will set the `usetex` parameter to `True` to enable the usetex mode.

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
