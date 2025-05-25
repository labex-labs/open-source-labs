# Criar o Gráfico

Nesta etapa, criaremos o gráfico usando os arrays mascarados criados na etapa anterior. Plotaremos cada array mascarado separadamente e usaremos cores diferentes para cada um.

```python
fig, ax = plt.subplots()
ax.plot(t, smiddle, t, slower, t, supper)
plt.show()
```
