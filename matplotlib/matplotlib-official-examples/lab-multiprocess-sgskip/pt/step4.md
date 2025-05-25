# Criar uma instância de `NBPlot` e enviar dados para `ProcessPlotter`

Crie uma instância da classe `NBPlot` e envie dados aleatórios para a classe `ProcessPlotter`. Enviaremos 10 conjuntos de dados, com um atraso de 0,5 segundos entre cada conjunto.

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
