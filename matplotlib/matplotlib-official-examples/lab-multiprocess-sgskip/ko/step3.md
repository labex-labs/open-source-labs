# `NBPlot` 클래스 정의

`NBPlot` 클래스는 임의의 데이터를 생성하여 파이프를 통해 `ProcessPlotter` 클래스로 전송합니다.

```python
class NBPlot:
    def __init__(self):
        self.plot_pipe, plotter_pipe = mp.Pipe()
        self.plotter = ProcessPlotter()
        self.plot_process = mp.Process(
            target=self.plotter, args=(plotter_pipe,), daemon=True)
        self.plot_process.start()

    def plot(self, finished=False):
        send = self.plot_pipe.send
        if finished:
            send(None)
        else:
            data = np.random.random(2)
            send(data)
```
