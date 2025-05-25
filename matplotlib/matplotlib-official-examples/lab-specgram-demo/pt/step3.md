# Gerar Espectrograma

Agora, geraremos um gráfico de espectrograma do sinal. Usaremos o método `specgram` da classe `Axes` do Matplotlib para gerar o espectrograma. Este método retorna quatro objetos: `Pxx`, `freqs`, `bins` e `im`. `Pxx` é o periodograma, `freqs` é o vetor de frequência, `bins` são os centros dos intervalos de tempo e `im` é a instância `AxesImage` que representa os dados no gráfico.

```python
NFFT = 1024  # the length of the windowing segments
Fs = int(1.0 / dt)  # the sampling frequency

fig, (ax1, ax2) = plt.subplots(nrows=2)
ax1.plot(t, x)
Pxx, freqs, bins, im = ax2.specgram(x, NFFT=NFFT, Fs=Fs, noverlap=900)
```
