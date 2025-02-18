# Génération de signaux

Nous devons générer deux signaux. Ces signaux contiennent une partie cohérente et une partie aléatoire. La partie cohérente des deux signaux a une fréquence de 10 Hz. La partie aléatoire des signaux est générée en utilisant du bruit blanc qui est passé à travers un filtre passe-bas pour créer du bruit coloré.

```python
dt = 0.01
t = np.arange(0, 30, dt)

# Fixing random state for reproducibility
np.random.seed(19680801)

nse1 = np.random.randn(len(t))                 # white noise 1
nse2 = np.random.randn(len(t))                 # white noise 2
r = np.exp(-t / 0.05)

cnse1 = np.convolve(nse1, r, mode='same') * dt   # colored noise 1
cnse2 = np.convolve(nse2, r, mode='same') * dt   # colored noise 2

# two signals with a coherent part and a random part
s1 = 0.01 * np.sin(2 * np.pi * 10 * t) + cnse1
s2 = 0.01 * np.sin(2 * np.pi * 10 * t) + cnse2
```
