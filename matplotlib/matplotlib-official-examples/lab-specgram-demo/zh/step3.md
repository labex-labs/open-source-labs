# 生成频谱图

现在我们将生成该信号的频谱图。我们将使用Matplotlib的`Axes`类中的`specgram`方法来生成频谱图。此方法返回四个对象：`Pxx`、`freqs`、`bins`和`im`。`Pxx`是周期图，`freqs`是频率向量，`bins`是时间区间的中心，`im`是表示图中数据的`AxesImage`实例。

```python
NFFT = 1024  # 加窗段的长度
Fs = int(1.0 / dt)  # 采样频率

fig, (ax1, ax2) = plt.subplots(nrows=2)
ax1.plot(t, x)
Pxx, freqs, bins, im = ax2.specgram(x, NFFT=NFFT, Fs=Fs, noverlap=900)
```
