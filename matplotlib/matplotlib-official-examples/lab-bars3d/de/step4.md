# Anpassen der Säulendiagramme

Wir werden nun die Säulendiagramme anpassen. Wir werden ein Array von Farben erstellen und die `bar()`-Methode verwenden, um die Säulendiagramme zu zeichnen. Wir werden den `zdir`-Parameter auf 'y' setzen, um die Säulendiagramme auf die Ebenen der y-Achse zu projizieren. Wir werden auch den `alpha`-Parameter auf 0,8 setzen, um die Transparenz der Säulen anzupassen.

```python
    cs = [c] * len(xs)
    cs[0] = 'c'
    ax.bar(xs, ys, zs=k, zdir='y', color=cs, alpha=0.8)
```
