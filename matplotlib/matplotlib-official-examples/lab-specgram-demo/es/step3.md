# Generar espectrograma

Ahora generaremos un gráfico de espectrograma de la señal. Utilizaremos el método `specgram` de la clase `Axes` de Matplotlib para generar el espectrograma. Este método devuelve cuatro objetos: `Pxx`, `freqs`, `bins` e `im`. `Pxx` es el periodograma, `freqs` es el vector de frecuencias, `bins` es el centro de los intervalos de tiempo e `im` es la instancia `AxesImage` que representa los datos en el gráfico.

```python
NFFT = 1024  # la longitud de los segmentos de ventanado
Fs = int(1.0 / dt)  # la frecuencia de muestreo

fig, (ax1, ax2) = plt.subplots(nrows=2)
ax1.plot(t, x)
Pxx, freqs, bins, im = ax2.specgram(x, NFFT=NFFT, Fs=Fs, noverlap=900)
```
