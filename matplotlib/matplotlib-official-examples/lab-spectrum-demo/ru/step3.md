# Создаем графики

Теперь мы создадим графики для наших различных представлений спектра. Используем функцию `subplots` библиотеки Matplotlib для создания сетки графиков размером 3x2. В первом графике будем отображать временной сигнал, а в оставшихся - различные виды спектров.

```python
fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(7, 7))

# рисуем временной сигнал:
axs[0, 0].set_title("Signal")
axs[0, 0].plot(t, s, color='C0')
axs[0, 0].set_xlabel("Time")
axs[0, 0].set_ylabel("Amplitude")

# рисуем различные виды спектров:
axs[1, 0].set_title("Magnitude Spectrum")
axs[1, 0].magnitude_spectrum(s, Fs=Fs, color='C1')

axs[1, 1].set_title("Log. Magnitude Spectrum")
axs[1, 1].magnitude_spectrum(s, Fs=Fs, scale='dB', color='C1')

axs[2, 0].set_title("Phase Spectrum ")
axs[2, 0].phase_spectrum(s, Fs=Fs, color='C2')

axs[2, 1].set_title("Angle Spectrum")
axs[2, 1].angle_spectrum(s, Fs=Fs, color='C2')

axs[0, 1].remove()  # не отображаем пустой ax

fig.tight_layout()
plt.show()
```
