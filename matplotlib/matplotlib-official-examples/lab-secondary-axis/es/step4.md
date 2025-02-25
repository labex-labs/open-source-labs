# Trazar otro ejemplo

Ahora trazaremos otro ejemplo de conversión de número de onda a longitud de onda en una escala log-log. Usaremos un espectro aleatorio para este ejemplo.

```python
fig, ax = plt.subplots(layout='constrained')
x = np.arange(0.02, 1, 0.02)
np.random.seed(19680801)
y = np.random.randn(len(x)) ** 2
ax.loglog(x, y)
ax.set_xlabel('f [Hz]')
ax.set_ylabel('PSD')
ax.set_title('Espectro aleatorio')
```
