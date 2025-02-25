# Erstellen der Figur

Der letzte Schritt besteht darin, die Figur mit der `plt.figure`-Funktion zu erstellen. Wir werden die Figurgröße auf (7, 4) setzen und die in Schritten 2 - 4 erstellte `curvelinear_test1`-Funktion aufrufen.

```python
if __name__ == "__main__":
    fig = plt.figure(figsize=(7, 4))
    curvelinear_test1(fig)
    plt.show()
```
