# Multiprocessing with Matplotlib

## Introduction

In this lab, you will learn how to use the multiprocessing library and Matplotlib to plot data generated from a separate process. We will create two classes - `ProcessPlotter` and `NBPlot` - to handle the plotting and data generation, respectively. The `NBPlot` class will generate random data and send it to the `ProcessPlotter` class through a pipe, which will then plot the data in real-time.

## Steps

### Step 1: Import Libraries

We begin by importing the necessary libraries. We will use `multiprocessing` to handle the separate processes, `time` for the time delay, `numpy` to generate random data, and `matplotlib` for the plotting.

```python
import multiprocessing as mp
import time
import numpy as np
import matplotlib.pyplot as plt
```

### Step 2: Define the `ProcessPlotter` Class

The `ProcessPlotter` class will handle the plotting of the data sent through the pipe. It will continuously check the pipe for new data and plot it in real-time.

```python
class ProcessPlotter:
    def __init__(self):
        self.x = []
        self.y = []

    def terminate(self):
        plt.close('all')

    def call_back(self):
        while self.pipe.poll():
            command = self.pipe.recv()
            if command is None:
                self.terminate()
                return False
            else:
                self.x.append(command[0])
                self.y.append(command[1])
                self.ax.plot(self.x, self.y, 'ro')
        self.fig.canvas.draw()
        return True

    def __call__(self, pipe):
        print('starting plotter...')

        self.pipe = pipe
        self.fig, self.ax = plt.subplots()
        timer = self.fig.canvas.new_timer(interval=1000)
        timer.add_callback(self.call_back)
        timer.start()

        print('...done')
        plt.show()
```

### Step 3: Define the `NBPlot` Class

The `NBPlot` class will generate random data and send it to the `ProcessPlotter` class through a pipe.

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

### Step 4: Create an instance of `NBPlot` and send data to `ProcessPlotter`

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

## Summary

In this lab, we learned how to use the `multiprocessing` library and Matplotlib to plot data generated from a separate process. We created two classes - `ProcessPlotter` and `NBPlot` - to handle the plotting and data generation, respectively. The `NBPlot` class generated random data and sent it to the `ProcessPlotter` class through a pipe, which then plotted the data in real-time.
