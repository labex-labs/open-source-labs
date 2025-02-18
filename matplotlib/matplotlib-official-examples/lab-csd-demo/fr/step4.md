# Calcul de la Densité Spectrale Croisée (CSD)

Pour calculer la Densité Spectrale Croisée (Cross Spectral Density - CSD) de deux signaux, nous devons utiliser la fonction `csd` de Matplotlib. Cette fonction prend en entrée les deux signaux, le nombre de points pour la Transformée de Fourier Rapide (Fast Fourier Transform - FFT) et la fréquence d'échantillonnage.

```python
fig, ax = plt.subplots()
cxy, f = ax.csd(s1, s2, 256, 1. / dt)
ax.set_ylabel('CSD (dB)')
plt.show()
```
