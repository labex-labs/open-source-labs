# Criar o Gráfico de Chapéu

Nesta etapa, criaremos o Gráfico de Chapéu usando os dados preparados na etapa anterior e a função `hat_graph`.

```python
fig, ax = plt.subplots()
hat_graph(ax, xlabels, [playerA, playerB], ['Player A', 'Player B'])

# Adicionar algum texto para rótulos, título e rótulos personalizados do eixo x, etc.
ax.set_xlabel('Jogos')
ax.set_ylabel('Pontuação')
ax.set_ylim(0, 60)
ax.set_title('Pontuações por número de jogo e jogadores')
ax.legend()

fig.tight_layout()
plt.show()
```
