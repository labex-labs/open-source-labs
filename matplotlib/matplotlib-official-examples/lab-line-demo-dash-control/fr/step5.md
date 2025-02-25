# Modifiez la séquence de traits discontinus à l'aide de `.Line2D.set_dashes()`

Nous pouvons modifier la séquence de traits discontinus à l'aide de `.Line2D.set_dashes()`. Dans cet exemple, nous modifions la séquence de traits discontinus pour `line1` pour créer un motif de traits discontinus de 2pt de ligne, 2pt de pause, 10pt de ligne et 2pt de pause. Nous définissons également le style de terminaison sur 'round' à l'aide de `line1.set_dash_capstyle()`.

```python
line1, = ax.plot(x, y, label='Using set_dashes() and set_dash_capstyle()')
line1.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break.
line1.set_dash_capstyle('round')
```
