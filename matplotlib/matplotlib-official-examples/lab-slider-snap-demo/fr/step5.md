# Créer les curseurs

Dans cette étape, vous allez créer les curseurs. Vous en créerez un pour l'amplitude et un pour la fréquence.

```python
samp = Slider(
    ax_amp, "Amp", 0.1, 9.0,
    valinit=a0, valstep=allowed_amplitudes,
    color="green"
)

sfreq = Slider(
    ax_freq, "Freq", 0, 10*np.pi,
    valinit=2*np.pi, valstep=np.pi,
    initcolor='none'  # Remove the line marking the valinit position.
)
```
