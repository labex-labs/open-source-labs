# Configurez les variables

Ensuite, nous allons configurer les variables pour notre signal. Nous utiliserons un intervalle d'échantillonnage de 0,01, ce qui nous donne une fréquence d'échantillonnage de 100 Hz. Nous allons créer un tableau de temps allant de 0 à 10 secondes avec un pas de 0,01 seconde. Nous allons également générer du bruit à l'aide de la fonction `randn` de NumPy et le convoluer avec une fonction de décroissance exponentielle pour créer un signal bruité.

```python
np.random.seed(0)

dt = 0.01  # intervalle d'échantillonnage
Fs = 1 / dt  # fréquence d'échantillonnage
t = np.arange(0, 10, dt)

# générer du bruit :
nse = np.random.randn(len(t))
r = np.exp(-t / 0.05)
cnse = np.convolve(nse, r) * dt
cnse = cnse[:len(t)]

s = 0.1 * np.sin(4 * np.pi * t) + cnse  # le signal
```
