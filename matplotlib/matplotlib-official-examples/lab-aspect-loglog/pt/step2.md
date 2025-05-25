# Criar um Gráfico Log-Log com Caixa Ajustável

Em seguida, criaremos um gráfico log-log com uma caixa ajustável. Isso significa que tanto o eixo x quanto o eixo y terão escalas logarítmicas, e a proporção do gráfico será igual a 1.

```python
fig, ax = plt.subplots()
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(1e1, 1e3)
ax.set_ylim(1e2, 1e3)
ax.set_aspect(1)
ax.set_title("Gráfico Log-Log com Caixa Ajustável")
plt.show()
```
