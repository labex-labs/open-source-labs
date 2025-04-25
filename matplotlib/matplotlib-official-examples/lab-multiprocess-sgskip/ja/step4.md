# 「NBPlot」のインスタンスを作成して、データを「ProcessPlotter」に送信する

「NBPlot」クラスのインスタンスを作成し、ランダムなデータを「ProcessPlotter」クラスに送信します。10 セットのデータを送信し、各セット間に 0.5 秒の遅延を設けます。

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
