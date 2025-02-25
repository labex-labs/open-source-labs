# Personalizar el gráfico

Podemos personalizar el gráfico agregando títulos, etiquetas de eje y mapas de colores.

```python
fig, (ax1, ax2) = plt.subplots(nrows=2)
ax1.set_title('Señal en el dominio del tiempo')
ax1.set_xlabel('Tiempo (s)')
ax1.set_ylabel('Amplitud')
ax1.plot(t, x)

ax2.set_title('Espectrograma')
ax2.set_xlabel('Tiempo (s)')
ax2.set_ylabel('Frecuencia (Hz)')
im = ax2.specgram(x, NFFT=NFFT, Fs=Fs, noverlap=900, cmap='viridis')
fig.colorbar(im[3], ax=ax2)
```
