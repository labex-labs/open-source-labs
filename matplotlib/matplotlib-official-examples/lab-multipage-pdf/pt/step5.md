# Criar a Terceira Página

Nesta etapa, você criará a terceira página do arquivo PDF. A página conterá um gráfico de uma parábola.

```python
plt.rcParams['text.usetex'] = False
fig = plt.figure(figsize=(4, 5))
plt.plot(x, x ** 2, 'ko')
plt.title('Page Three')
pdf.savefig(fig)  # or you can pass a Figure object to pdf.savefig
plt.close()
```
