# Crear la tercera página

En este paso, creará la tercera página del archivo PDF. La página contendrá un gráfico de una parábola.

```python
plt.rcParams['text.usetex'] = False
fig = plt.figure(figsize=(4, 5))
plt.plot(x, x ** 2, 'ko')
plt.title('Page Three')
pdf.savefig(fig)  # o puede pasar un objeto Figure a pdf.savefig
plt.close()
```
