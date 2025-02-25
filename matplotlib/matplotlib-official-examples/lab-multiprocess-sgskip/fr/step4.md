# Créer une instance de `NBPlot` et envoyer des données à `ProcessPlotter`

Créez une instance de la classe `NBPlot` et envoyez des données aléatoires à la classe `ProcessPlotter`. Nous enverrons 10 ensembles de données, avec un délai de 0,5 seconde entre chaque ensemble.

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
