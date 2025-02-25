# Créez des graphiques

Maintenant, nous allons créer les graphiques pour nos différentes représentations du spectre. Nous utiliserons la fonction `subplots` de Matplotlib pour créer une grille de 3x2 de graphiques. Nous traçons le signal temporel dans le premier graphique et les différents types de spectre dans les graphiques restants.

```python
fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(7, 7))

# tracez le signal temporel :
axs[0, 0].set_title("Signal")
axs[0, 0].plot(t, s, color='C0')
axs[0, 0].set_xlabel("Temps")
axs[0, 0].set_ylabel("Amplitude")

# tracez différents types de spectre :
axs[1, 0].set_title("Spectre d'amplitude")
axs[1, 0].magnitude_spectrum(s, Fs=Fs, color='C1')

axs[1, 1].set_title("Spectre d'amplitude logarithmique")
axs[1, 1].magnitude_spectrum(s, Fs=Fs, scale='dB', color='C1')

axs[2, 0].set_title("Spectre de phase ")
axs[2, 0].phase_spectrum(s, Fs=Fs, color='C2')

axs[2, 1].set_title("Spectre d'angle")
axs[2, 1].angle_spectrum(s, Fs=Fs, color='C2')

axs[0, 1].remove()  # ne pas afficher l'axe vide

fig.tight_layout()
plt.show()
```
