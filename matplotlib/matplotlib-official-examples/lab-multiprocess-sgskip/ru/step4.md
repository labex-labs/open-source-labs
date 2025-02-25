# Создайте экземпляр `NBPlot` и отправьте данные в `ProcessPlotter`

Создайте экземпляр класса `NBPlot` и отправьте случайные данные в класс `ProcessPlotter`. Мы отправим 10 наборов данных с задержкой в 0,5 секунды между каждым набором.

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
