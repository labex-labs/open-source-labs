# Erstelle eine Instanz von `NBPlot` und sende Daten an `ProcessPlotter`

Erstelle eine Instanz der Klasse `NBPlot` und sende zufällige Daten an die Klasse `ProcessPlotter`. Wir werden 10 Datensätze senden, mit einer Verzögerung von 0,5 Sekunden zwischen jedem Satz.

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
