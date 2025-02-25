# Crear la segunda página

En este paso, creará la segunda página del archivo PDF. La página contendrá un gráfico de una onda sinusoidal.

```python
plt.rcParams['text.usetex'] = True
plt.figure(figsize=(8, 6))
x = np.arange(0, 5, 0.1)
plt.plot(x, np.sin(x), 'b-')
plt.title('Page Two')
pdf.attach_note("plot of sin(x)")  # adjuntar metadatos (como nota de pdf) a la página
pdf.savefig()
plt.close()
```
