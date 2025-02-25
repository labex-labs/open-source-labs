# Создаем график

В этом шаге мы создадим график. Мы будем использовать метод `fig.text()`, чтобы добавить текст на график. Мы будем перебирать список шрифтов и соответствующего текста, используя функцию `zip()`, чтобы сопоставить их. Мы установим параметр `usetex` в значение `True`, чтобы включить режим usetex.

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
