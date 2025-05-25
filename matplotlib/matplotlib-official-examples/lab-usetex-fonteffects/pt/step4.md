# Criar o Gráfico

Nesta etapa, criaremos o gráfico. Usaremos o método `fig.text()` para adicionar texto ao gráfico. Iteraremos sobre uma lista de fontes e o texto correspondente, usando a função `zip()` para combiná-los. Definiremos o parâmetro `usetex` como `True` para habilitar o modo usetex.

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
