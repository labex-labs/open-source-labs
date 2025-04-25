# グラフを作成する

ここでは、さまざまなスペクトル表現のグラフを作成します。Matplotlib の`subplots`関数を使って、3x2 のグリッドのグラフを作成します。最初のグラフには時間信号をプロットし、残りのグラフにはさまざまなスペクトルタイプをプロットします。

```python
fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(7, 7))

# 時間信号をプロットする：
axs[0, 0].set_title("Signal")
axs[0, 0].plot(t, s, color='C0')
axs[0, 0].set_xlabel("Time")
axs[0, 0].set_ylabel("Amplitude")

# さまざまなスペクトルタイプをプロットする：
axs[1, 0].set_title("Magnitude Spectrum")
axs[1, 0].magnitude_spectrum(s, Fs=Fs, color='C1')

axs[1, 1].set_title("Log. Magnitude Spectrum")
axs[1, 1].magnitude_spectrum(s, Fs=Fs, scale='dB', color='C1')

axs[2, 0].set_title("Phase Spectrum ")
axs[2, 0].phase_spectrum(s, Fs=Fs, color='C2')

axs[2, 1].set_title("Angle Spectrum")
axs[2, 1].angle_spectrum(s, Fs=Fs, color='C2')

axs[0, 1].remove()  # 空の ax を表示しない

fig.tight_layout()
plt.show()
```
