# Criar a Primeira Página

Nesta etapa, você criará a primeira página do arquivo PDF. A página conterá um gráfico de um gráfico simples.

```python
plt.figure(figsize=(3, 3))
plt.plot(range(7), [3, 1, 4, 1, 5, 9, 2], 'r-o')
plt.title('Page One')
pdf.savefig()
plt.close()
```
