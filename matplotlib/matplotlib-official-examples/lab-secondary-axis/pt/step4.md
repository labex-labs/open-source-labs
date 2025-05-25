# Plotar outro exemplo

Agora plotaremos outro exemplo de conversão de número de onda (wavenumber) para comprimento de onda (wavelength) em uma escala log-log. Usaremos um espectro aleatório para este exemplo.

```python
fig, ax = plt.subplots(layout='constrained')
x = np.arange(0.02, 1, 0.02)
np.random.seed(19680801)
y = np.random.randn(len(x)) ** 2
ax.loglog(x, y)
ax.set_xlabel('f [Hz]')
ax.set_ylabel('PSD')
ax.set_title('Random spectrum')
```
