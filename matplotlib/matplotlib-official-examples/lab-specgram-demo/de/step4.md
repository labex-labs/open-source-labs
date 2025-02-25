# Plot anpassen

Wir können den Plot anpassen, indem wir Titel, Achsenbeschriftungen und Farbskalen hinzufügen.

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
