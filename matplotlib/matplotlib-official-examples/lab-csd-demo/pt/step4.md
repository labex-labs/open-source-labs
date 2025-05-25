# Calcular CSD

Para calcular a CSD (Cross Spectral Density) de dois sinais, precisamos usar a função `csd` do Matplotlib. A função recebe os dois sinais, o número de pontos para a FFT (Fast Fourier Transform) e a frequência de amostragem como entradas.

```python
fig, ax = plt.subplots()
cxy, f = ax.csd(s1, s2, 256, 1. / dt)
ax.set_ylabel('CSD (dB)')
plt.show()
```
