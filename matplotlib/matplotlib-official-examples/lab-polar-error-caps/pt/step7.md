# Criar Barras de Erro de Raio Grandes

Nesta etapa, criaremos barras de erro de raio grandes para demonstrar como elas podem levar a uma escala indesejada nos dados, reduzindo a faixa exibida.

```python
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection='polar')
ax.errorbar(theta, r, xerr=0.25, yerr=10.1, capsize=7, fmt="o", c="orangered")
ax.set_title("Large Radius Error Bars")
plt.show()
```
