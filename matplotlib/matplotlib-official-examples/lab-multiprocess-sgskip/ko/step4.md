# `NBPlot` 인스턴스 생성 및 `ProcessPlotter`에 데이터 전송

`NBPlot` 클래스의 인스턴스를 생성하고 임의의 데이터를 `ProcessPlotter` 클래스로 전송합니다. 10 개의 데이터 세트를 전송하며, 각 세트 사이에는 0.5 초의 지연이 있습니다.

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
