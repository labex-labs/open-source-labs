# Criar os Sliders (Barras Deslizantes)

Agora criaremos os sliders (barras deslizantes) que nos permitirão ajustar a frequência e a amplitude da onda senoidal. Criaremos um slider horizontal para controlar a frequência e um slider vertical para controlar a amplitude.

```python
fig.subplots_adjust(left=0.25, bottom=0.25)
axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
freq_slider = Slider(
    ax=axfreq,
    label='Frequency [Hz]',
    valmin=0.1,
    valmax=30,
    valinit=init_frequency,
)

axamp = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
amp_slider = Slider(
    ax=axamp,
    label="Amplitude",
    valmin=0,
    valmax=10,
    valinit=init_amplitude,
    orientation="vertical"
)
```
