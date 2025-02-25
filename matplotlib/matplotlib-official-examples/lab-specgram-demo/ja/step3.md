# スペクトログラムの生成

次に、信号のスペクトログラムを生成します。Matplotlibの`Axes`クラスの`specgram`メソッドを使ってスペクトログラムを生成します。このメソッドは4つのオブジェクトを返します：`Pxx`、`freqs`、`bins`、および`im`。`Pxx`は周期グラム、`freqs`は周波数ベクトル、`bins`は時間ビンの中心、`im`はプロット内のデータを表す`AxesImage`インスタンスです。

```python
NFFT = 1024  # the length of the windowing segments
Fs = int(1.0 / dt)  # the sampling frequency

fig, (ax1, ax2) = plt.subplots(nrows=2)
ax1.plot(t, x)
Pxx, freqs, bins, im = ax2.specgram(x, NFFT=NFFT, Fs=Fs, noverlap=900)
```
