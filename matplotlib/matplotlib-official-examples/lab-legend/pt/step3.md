# Criando o Gráfico

Agora estamos prontos para criar nosso gráfico. Usaremos a função `plot` do Matplotlib para plotar três linhas no mesmo gráfico, cada uma com um rótulo predefinido. Usaremos o parâmetro `label` para atribuir os rótulos a cada linha.

```python
# Create plots with pre-defined labels.
fig, ax = plt.subplots()
ax.plot(a, c, 'k--', label='Model length')
ax.plot(a, d, 'k:', label='Data length')
ax.plot(a, c + d, 'k', label='Total message length')
```
