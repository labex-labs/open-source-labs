# Create an instance of `NBPlot` and send data to `ProcessPlotter`

Create an instance of the `NBPlot` class and send random data to the `ProcessPlotter` class. We will send 10 sets of data, with a 0.5 second delay between each set.

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
