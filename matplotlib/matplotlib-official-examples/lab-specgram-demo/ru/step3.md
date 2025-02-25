# Генерация спектрограммы

Теперь мы сгенерируем график спектрограммы сигнала. Мы будем использовать метод `specgram` из класса `Axes` Matplotlib для генерации спектрограммы. Этот метод возвращает четыре объекта: `Pxx`, `freqs`, `bins` и `im`. `Pxx` — это периодограмма, `freqs` — это вектор частот, `bins` — это центры временных интервалов, а `im` — это экземпляр `AxesImage`, представляющий данные на графике.

```python
NFFT = 1024  # the length of the windowing segments
Fs = int(1.0 / dt)  # the sampling frequency

fig, (ax1, ax2) = plt.subplots(nrows=2)
ax1.plot(t, x)
Pxx, freqs, bins, im = ax2.specgram(x, NFFT=NFFT, Fs=Fs, noverlap=900)
```
