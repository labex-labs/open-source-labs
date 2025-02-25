# Crear gráficos

Ahora crearemos los gráficos para nuestras diferentes representaciones del espectro. Utilizaremos la función `subplots` de Matplotlib para crear una cuadrícula de 3x2 de gráficos. Graficaremos la señal en el primer gráfico y los diferentes tipos de espectro en los gráficos restantes.

```python
fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(7, 7))

# graficar la señal en el tiempo:
axs[0, 0].set_title("Señal")
axs[0, 0].plot(t, s, color='C0')
axs[0, 0].set_xlabel("Tiempo")
axs[0, 0].set_ylabel("Amplitud")

# graficar diferentes tipos de espectro:
axs[1, 0].set_title("Espectro de Magnitud")
axs[1, 0].magnitude_spectrum(s, Fs=Fs, color='C1')

axs[1, 1].set_title("Espectro de Magnitud Logarítmica")
axs[1, 1].magnitude_spectrum(s, Fs=Fs, scale='dB', color='C1')

axs[2, 0].set_title("Espectro de Fase ")
axs[2, 0].phase_spectrum(s, Fs=Fs, color='C2')

axs[2, 1].set_title("Espectro de Ángulo")
axs[2, 1].angle_spectrum(s, Fs=Fs, color='C2')

axs[0, 1].remove()  # no mostrar el eje vacío

fig.tight_layout()
plt.show()
```
