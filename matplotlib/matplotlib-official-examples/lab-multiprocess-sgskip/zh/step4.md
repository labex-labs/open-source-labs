# 创建 `NBPlot` 实例并将数据发送到 `ProcessPlotter`

创建 `NBPlot` 类的实例，并将随机数据发送到 `ProcessPlotter` 类。我们将发送 10 组数据，每组数据之间延迟 0.5 秒。

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
