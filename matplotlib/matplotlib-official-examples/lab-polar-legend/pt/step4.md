# Plotar Dados

Agora podemos plotar nossos dados usando a função `plot`. Criaremos duas linhas usando os dados que criamos no passo 3.

```python
ax.plot(theta, r, color="tab:orange", lw=3, label="a line")
ax.plot(0.5 * theta, r, color="tab:blue", ls="--", lw=3, label="another line")
```
