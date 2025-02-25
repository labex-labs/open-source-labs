# Erstellen der Schieberegler

Wir werden nun die Schieberegler erstellen, die uns ermöglichen, die Frequenz und die Amplitude der Sinuswelle anzupassen. Wir werden einen horizontalen Schieberegler erstellen, um die Frequenz zu steuern, und einen vertikalen Schieberegler, um die Amplitude zu steuern.

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
