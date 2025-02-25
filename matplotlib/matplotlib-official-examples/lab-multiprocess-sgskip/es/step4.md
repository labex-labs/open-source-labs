# Crear una instancia de `NBPlot` y enviar datos a `ProcessPlotter`

Crea una instancia de la clase `NBPlot` y envía datos aleatorios a la clase `ProcessPlotter`. Enviaremos 10 conjuntos de datos, con una demora de 0,5 segundos entre cada conjunto.

```python
def main():
    pl = NBPlot()
    for _ in range(10):
        pl.plot()
        time.sleep(0.5)
    pl.plot(finished=True)

if __name__ == '__main__':
    if plt.get_backend() == "MacOSX":
        mp.set_start_method("forkserver")
    main()
```
