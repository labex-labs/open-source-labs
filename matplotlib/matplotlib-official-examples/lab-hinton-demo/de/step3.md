# Erzeugen eines Hinton-Diagramms

Jetzt werden wir mithilfe von numpy eine zufällige Gewichtsmatrix erzeugen und dann die `hinton`-Funktion verwenden, um das Hinton-Diagramm zu erzeugen.

```python
if __name__ == '__main__':
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    hinton(np.random.rand(20, 20) - 0.5)
    plt.show()
```
