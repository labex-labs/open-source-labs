# Erstelle die Schieberegler

In diesem Schritt wirst du die Schieberegler erstellen. Du wirst einen Schieberegler für die Amplitude und einen Schieberegler für die Frequenz erstellen.

```python
samp = Slider(
    ax_amp, "Amp", 0.1, 9.0,
    valinit=a0, valstep=allowed_amplitudes,
    color="green"
)

sfreq = Slider(
    ax_freq, "Freq", 0, 10*np.pi,
    valinit=2*np.pi, valstep=np.pi,
    initcolor='none'  # Entferne die Linie, die die valinit-Position markiert.
)
```
