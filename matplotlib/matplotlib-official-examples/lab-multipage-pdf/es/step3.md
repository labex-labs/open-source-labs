# Crear la primera página

En este paso, creará la primera página del archivo PDF. La página contendrá un gráfico de una gráfica simple.

```python
plt.figure(figsize=(3, 3))
plt.plot(range(7), [3, 1, 4, 1, 5, 9, 2], 'r-o')
plt.title('Page One')
pdf.savefig()
plt.close()
```
