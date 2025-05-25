# 플롯 사용자 정의

제목, 축 레이블 및 컬러 맵을 추가하여 플롯을 사용자 정의할 수 있습니다.

```python
fig, (ax1, ax2) = plt.subplots(nrows=2)
ax1.set_title('Time Domain Signal')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Amplitude')
ax1.plot(t, x)

ax2.set_title('Spectrogram')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Frequency (Hz)')
im = ax2.specgram(x, NFFT=NFFT, Fs=Fs, noverlap=900, cmap='viridis')
fig.colorbar(im[3], ax=ax2)
```
