# Gerar Sinal

Em seguida, geraremos um sinal para plotar. Neste exemplo, criaremos um sinal que é a soma de duas ondas senoidais com diferentes frequências e algum ruído aleatório.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

dt = 0.0005
t = np.arange(0.0, 20.0, dt)
s1 = np.sin(2 * np.pi * 100 * t)
s2 = 2 * np.sin(2 * np.pi * 400 * t)

# create a transient "chirp"
s2[t <= 10] = s2[12 <= t] = 0

# add some noise into the mix
nse = 0.01 * np.random.random(size=len(t))

x = s1 + s2 + nse  # the signal
```
